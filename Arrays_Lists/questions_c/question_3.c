#include <stdio.h>
#include <stdlib.h>

int* middle(int* lst, int length);

int main() {
    int myList[] = {1, 2, 3, 4}, length;
    int* result;
    length = sizeof(myList) / sizeof(myList[0]);
    result = middle(myList, length);
    int result_length = sizeof(result) / sizeof(result[0]);

    printf("[");
    for(int i = 0; i < result_length; i++) {
        if(i != result_length-1) {
            printf("%d, ", result[i]);
        } else {
            printf("%d", result[i]);
        }
    }
    printf("]\n");
    free(result);
    return 0;
}

int* middle(int* lst, int length) {
    int* arr = (int*)malloc(100 * sizeof(int));
    int count = 0;
    for(int i = 1; i < length-1; i++) {
        arr[count] = lst[i];
        count++;
    }
    return arr;
    
}