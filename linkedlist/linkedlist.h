#include <stdio.h>
#include <stdlib.h>

#define BOOL int
#define FALSE 0
#define TRUE 1

struct struct_LinkedList{
    int data;
    struct struct_LinkedList *next;
};
typedef struct struct_LinkedList linkedlist;

BOOL init_linkedlist(linkedlist **list);
BOOL add_element(linkedlist **list, int data);
BOOL print_list(linkedlist *list);

BOOL print_middle(linkedlist *list);
BOOL delete_middle(linkedlist *list);