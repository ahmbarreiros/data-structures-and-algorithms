def diagonal_sum(matrix):
    diagonal = 0
    for i in range(len(matrix)):
        diagonal += matrix[i][i]
    return diagonal