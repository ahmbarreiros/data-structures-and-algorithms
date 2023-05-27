def rotate(matrix):
    matrix_copy = matrix.copy()
    # TODO
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix_copy[i][j]
            matrix_copy[i][j] = matrix_copy[j][i]
            matrix_copy[j][i] = temp
    print(matrix_copy)
    for i in range(n):
        for j in range(n // 2):
            k = n - j - 1
            temp = matrix_copy[i][k]
            matrix_copy[i][k] = matrix_copy[i][j]
            matrix_copy[i][j] = temp
    return matrix_copy

        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

# 1 4 7
# 2 5 8
# 3 6 9