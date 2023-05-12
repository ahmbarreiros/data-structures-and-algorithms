#include <stdio.h>

void sum_pairs(int arr[], int n);

int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, n = 10, result;
    sum_pairs(nums, n);
    return 0;
}

void sum_pairs(int arr[], int n) {
    for(int i = 0; i < (n/2); i++) {
        for(int j = i + 1; j < n; j++) {
            if ((arr[i] + arr[j]) == n) {
                printf("(%d, %d)\n", arr[i], arr[j]);
            }
        }
    }
}