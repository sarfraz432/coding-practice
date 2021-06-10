#include "helper.h"


BOOL read_array(int **array, int size) {
    int i;
    int *temp_array;
    
    temp_array = malloc(size * sizeof(int));
    if (temp_array == NULL) {
        return FALSE;
    }
    printf("Please enter %d numbers : \n", size);
    for (i = 0; i < size; i++) {
        scanf("%d", &temp_array[i]);
    }

    *array = temp_array;
    return TRUE;
}
BOOL display_array(int *array, int size) {
    int i;

    printf("[");
    if (size > 0) {
        for (i = 0; i < size - 1; i++) {
            printf("%d, ", array[i]);
        }
        printf("%d", array[i]);
    }

    printf("]\n");

    return TRUE;
}