#include <stdio.h>

int diagonal_sum(int n, int* matrix);

int main() {
    int result, n=3;
    int mat[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    result = diagonal_sum(n, (int*)mat);
    printf("%d\n", result);
    return 0;
}

int diagonal_sum(int n, int* matrix) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        sum += *((matrix + i * n) + i);
    }
    return sum;
}