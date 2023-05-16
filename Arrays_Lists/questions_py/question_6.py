def remove_duplicates(arr):
    # return list(set(arr))
    filtered_array = []
    for i in range(len(arr)):
        isRepeated = False
        for j in range(len(filtered_array)):
            if arr[i] == filtered_array[j]:
                isRepeated = True
        if not isRepeated:
            filtered_array.append(arr[i])
    return filtered_array
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))