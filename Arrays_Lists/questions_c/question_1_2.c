#include <stdio.h>

void findNumber(int* nums, int n, int length);

int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, n = 8;
    int length = sizeof(nums) / sizeof(nums[0]);
    findNumber(nums, n, length);
    return 0;
}

void findNumber(int* nums, int n, int length) {
    printf("length %d\n", length);
    for(int i = 0; i < length; i++) {
        if(nums[i] == n) {
            printf("%d", i);
            return;
        }
    }
}