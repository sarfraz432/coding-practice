
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define BOOL int

int check_missing_number(int *array, int size){
    int i = 0, sum = 0, needed_sum;
    for (i = 0;  i < size; i++){
        sum += array[i];
    }
    int n = size + 1;
    needed_sum = (n * (n + 1))/2;
    if (n == needed_sum - sum){
        return 0;
    }
    return needed_sum - sum;
}

int main(int argc, char ** argv) {
    int *array;
    int size, i, num;


    if (argc < 2) {
        printf("Please provide size of array as parameter\n");
        return 0;
    }
    size = atoi(argv[1]);
    if (size <= 0) {
        printf("Size should be greater than 0\n");
        return 0;
    }
    array = malloc(size * sizeof(int));
    if (array == NULL) {
        return FALSE;
    }
    printf("Please enter %d numbers : \n", size);
    for (i = 0; i < size; i++) {
        scanf("%d", &array[i]);
    }

    num = check_missing_number(array, size);
    printf("Missing number is %d\n", num);
}