def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]
