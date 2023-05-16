#include <stdio.h>
#include <stdlib.h>

int* first_second(int* array, int length);

int main() {
    int myArray[] = {84,85,86,87,85,90,85,83,23,45,84,1,2,0};
    int* result;
    int arr_length = sizeof(myArray) / sizeof(myArray[0]);
    result = first_second(myArray, arr_length);
    printf("[%d, %d]\n", result[0], result[1]);
    free(result);
    return 0;
}

int* first_second(int* array, int length) {
    int max1 = array[0], max2 = array[1];
    int* max_array = (int*)malloc(sizeof(int));
    for(int i = 0; i < length; i++) {
        if(array[i] > max1 && array[i] > max2) {
            max2 = max1;
            max1 = array[i];
        } else if(array[i] > max2) {
            max2 = array[i];
        }
    }
    max_array[0] = max1;
    max_array[1] = max2;
    return max_array;
}