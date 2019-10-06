from Matrix import Matrix

matrix1 = Matrix(4, 5, initValue=6)
matrix2 = Matrix(5, 5, initValue=2)
matrix3 = Matrix(4, 5, initValue=2)
matrix3.copy(matrix1*matrix2)
print(matrix1)
print(matrix2)
print(matrix3)

