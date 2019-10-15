import random
import operator
import sys
import unittest

__version__ = "0.1"

class Matrix:
    '''
    This class can only create matricies
    Warning: please do not overwhelm the constructor with more then 2 dimensions
    '''
    def __init__(self, Content=[], dims=[2,2], initValue=0):
        self.shape = dims
        if Content:
            self.Content = Content
            self.shape = [len(self.Content[0]), len(self.Content)]
        else:
            self.Content = self.CreateMatrix(initValue)

    def __str__(self):
        for i in self.Content:
            print(i)
        return f"Printed matrix of dimensions: {self.shape[0]}, {self.shape[1]}!"

    def __getitem__(self, idx):
        return self.Content[idx]

    def __add__(self, other):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        if not isinstance(other, Matrix):
            raise "Matricies can only operate with other Matricies!"

        if self.shape != other.shape:
            raise "Trying to add matrixes of varying dimensions!"

        result = Matrix(dims = [self.shape[0], self.shape[1]])

        for x in range(self.shape[0]):
            row = [sum(item) for item in zip(self.Content[x], other[x])]
            result[x] = row

        return result

    def __sub__(self, other):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        if not isinstance(other, Matrix):
            raise "Matricies can only operate with other Matricies!"

        if self.shape != other.shape:
            raise "Trying to add matrixes of varying dimensions!"

        result = Matrix(dims = [self.shape[0], self.shape[1]])

        for x in range(self.shape[0]):
            row = [item[0]-item[1] for item in zip(self.Content[x], other[x])]
            result[x] = row

        return result

    def __mul__(self, other):
            """ Multiple a matrix with this matrix and
            return the new matrix. Doesn't modify
            the current matrix """
            if not isinstance(other, Matrix):
                raise "Matricies can only operate with other Matricies!"

            otherM, otherN = other.shape

            if (self.shape[1] != otherM):
                raise "Matrices cannot be multipled!"

            otherT = other.getTranspose()
            result = Matrix(dims = [self.shape[0], otherN])

            for x in range(self.shape[0]):
                for y in range(otherT.shape[0]):
                    result[x][y] = sum([item[0]*item[1] for item in list(zip(self.Content[x], otherT[y]))])

            return result

    def __setitem__(self, idx, item):
        self.Content[idx] = item

    def __repr__(self):
        s=str(self.Content)
        rep="Matrix: \"%r\", shape: \"%r\ %r\ " % (s[0], self.shape)
        return rep

    def reset(self):
        """ Reset the matrix data """
        self.Content = [[] for x in range(self.shape[0])]

    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """

        self.shape[0], self.shape[1] = self.shape[1], self.shape[0]
        self.Content = [list(item) for item in zip(*self.Content)]

    def getTranspose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        m, n = self.shape[1], self.shape[0]
        result = Matrix(dims=[m, n])
        result.Content =  [list(item) for item in zip(*self.Content)]

        return result

    def __len__(self):
        return self.shape

    def copy(self, other):
        self.Content = [[other[i][j] for j in range(len(other[0]))] for i in range(len(other))]
        self.dims = (len(self.Content[0]), len(self.Content))

    def append(self, other):
        self.Content.append(other)

    def CreateMatrix(self, initValue=0):
        M = [[initValue for j in range(self.shape[1])] for i in range(self.shape[0])]
        return M

matrix1 = Matrix(Content = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
matrix2 = Matrix(Content = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
matrix3 = Matrix(Content = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(matrix1)
print(matrix2)
print(matrix1 * matrix2)
print(matrix1 + matrix2)
print(matrix1 - matrix2)
print(matrix3.getTranspose())
matrix3.transpose()
print(matrix3)
