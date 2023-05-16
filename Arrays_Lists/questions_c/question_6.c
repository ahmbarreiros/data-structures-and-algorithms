#include <stdio.h>
#include <stdlib.h>

void remove_duplicates(int* array, int length);

int main() {
    int my_array[] = {1, 1, 2, 2, 3, 4, 5};
    int array_length = sizeof(my_array) / sizeof(my_array[0]);
    remove_duplicates(my_array, array_length);
    return 0;
}

void remove_duplicates(int* array, int length) {
    int* filtered_array = (int*)malloc(length*sizeof(int));
    int isRepeated;
    int filtered_array_length = sizeof(filtered_array);
    int count = 0;
    for(int i = 0; i < length; i++) {
        isRepeated = 0;
        for(int j = 0; j < filtered_array_length; j++) {
            if(array[i] == filtered_array[j]) {
                isRepeated = 1;
            }
        }
        if(isRepeated == 0) {
            filtered_array[count] = array[i];
            count++;
        }
    }

    printf("[");
    for(int i = 0; i < count; i++) {
        if(i != count-1) {
            printf("%d, ", filtered_array[i]);
        } else {
            printf("%d", filtered_array[i]);
        }
    }
    printf("]\n");
}