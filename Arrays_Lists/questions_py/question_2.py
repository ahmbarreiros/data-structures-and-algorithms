def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))