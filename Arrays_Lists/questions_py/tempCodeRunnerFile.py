def sum_of_pairs(arr, n):
    for i in range(len(arr) // 2):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                print([arr[i], arr[j]])
sum_of_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)