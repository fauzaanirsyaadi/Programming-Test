import random

# function to create a random matrix of size MxN
def create_matrix(M, N):
    return [[random.randint(1, 10) for j in range(N)] for i in range(M)]

# function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# sample usage
M = 4
N = 3
matrix1 = create_matrix(M, N)
matrix2 = create_matrix(N, M)
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
result = multiply_matrices(matrix1, matrix2)
print("Result:")
print(result)
