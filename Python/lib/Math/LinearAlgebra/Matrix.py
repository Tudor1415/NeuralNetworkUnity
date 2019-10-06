class Matrix:
    '''
    This class can only create 2D matricies, in this early dev stage
    Warning: please do not overwhelm the constructor with more then 2 dimensions
    '''
    def __init__(self, *dims, initValue=0):
        self.dimensions = dims
        self.Content = self.CreateMatrix(initValue)

    def __str__(self):
        for i in self.Content:
            print(i)
        return f"Printed matrix of dimensions: {self.dimensions[0]}, {self.dimensions[1]} !"

    def __getitem__(self, item):
        return self.Content[item]

    def __add__(self, other):
        if self.dimensions[0] == other.dimensions[0] and self.dimensions[1] == other.dimensions[1]:
            R = [[self.Content[i][j] + other.Content[i][j] for j in range(self.dimensions[1])] for i in range(self.dimensions[0])]
            return R
        else:
            print("WARNING! You can not multiply this two matricies!")
            return False

    def __sub__(self, other):
        if self.dimensions[0] == other.dimensions[0] and self.dimensions[1] == other.dimensions[1]:
            R = [[self.Content[i][j] - other.Content[i][j] for j in range(self.dimensions[1])] for i in range(self.dimensions[0])]
            return R
        else:
            print("WARNING! You can not multiply this two matricies!")
            return False

    def __mul__(self, other):
        if self.dimensions[0] == other.dimensions[1] or self.dimensions[1] == other.dimensions[0]:
            R = [[self.Content[i][j] * other.Content[j][i] for j in range(self.dimensions[1])] for i in range(self.dimensions[0])]
            return R
        else:
            print("WARNING! You can not multiply this two matricies!")
            return False

    def copy(self, other):
        self.Content = [[other[i][j] for j in range(len(other[0]))] for i in range(len(other))]

    def append(self, other):
        self.Content.append(other)

    def CreateMatrix(self, initValue=0):
        M = [[initValue for j in range(self.dimensions[1])] for i in range(self.dimensions[0])]
        return M