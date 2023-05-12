#include <stdio.h>

int max_product(int* arr, int length);

int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, result;
    int length = sizeof(nums) / sizeof(nums[0]);
    result = max_product(nums, length);
    printf("result: %d", result);
    return 0;
}

int max_product(int* arr, int length) {
    int max1 = 0, max2 = 0;
    for(int i = 0; i < length; i++) {
        if(arr[i] > max1) {
            max2 = max1;
            max1 = arr[i];
        } else if(arr[i] > max2) max2 = arr[i];
    }
    return max1*max2;
}