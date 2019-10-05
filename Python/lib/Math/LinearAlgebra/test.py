from Matrix import Matrix

matrix1 = Matrix(4, 5, initValue=1)
matrix2 = Matrix(5, 5, initValue=2)
# matrix3 = matrix1 * matrix2
# print(matrix1)
# print(matrix2)
# print(matrix3)

for i in range(4):
    for j in range(5):
        matrix1.Content[i][j] = 3
print(matrix1[1][4])