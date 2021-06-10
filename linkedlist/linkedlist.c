#include "linkedlist.h"


int main()
{
    linkedlist *list;

    init_linkedlist(&list);

    add_element(&list, 10);
    add_element(&list, 20);
    add_element(&list, 30);
    // add_element(&list, 40);
    // add_element(&list, 50);
    print_list(list);
    print_middle(list);
    delete_middle(list);
    print_list(list);
    return 0;
}


BOOL init_linkedlist(linkedlist **list) {
    *list = NULL;
    
    return TRUE;
}


BOOL add_element(linkedlist **list, int data) {
    // create new node
    linkedlist *new_node, *temp;
    new_node = malloc(sizeof(linkedlist));
    if (new_node == NULL){
        return FALSE;
    }
    new_node->data = data;
    new_node->next = NULL;

    // if list is empty
    if (*list == NULL) {
        *list = new_node;
        return TRUE;
    }
    temp = *list;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = new_node;
    return TRUE;
}


BOOL print_list(linkedlist *list){
    linkedlist *temp;
    if (list == NULL) {
        return FALSE;
    }
    temp = list;

    while(temp){
        printf("%d\n", temp->data);
        temp = temp->next;
    }
    return TRUE;

}


BOOL print_middle(linkedlist *list){
    linkedlist *slow_pointer, *fast_pointer;

    slow_pointer = list;
    fast_pointer = list;
    while(fast_pointer != NULL){
        fast_pointer = fast_pointer->next;
        if (fast_pointer == NULL)
            break;
        else
            fast_pointer = fast_pointer->next;
        slow_pointer = slow_pointer->next;
    }
    printf("Middle : %d\n",slow_pointer->data);
}


BOOL delete_middle(linkedlist *list){
    linkedlist *slow_pointer, *fast_pointer, *temp;

    slow_pointer = list;
    temp = list;
    fast_pointer = list;
    while(fast_pointer != NULL){
        fast_pointer = fast_pointer->next;
        if (fast_pointer == NULL)
            break;
        else
            fast_pointer = fast_pointer->next;
        temp = slow_pointer;
        slow_pointer = slow_pointer->next;
    }
    // printf("temp : %d\n", temp->data);
    // printf("slow_pointer : %d\n", slow_pointer->data);

    temp->next = slow_pointer->next;
    free(slow_pointer);
    return TRUE;
}