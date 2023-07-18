# Взять класс Матрица (написанный ранее)
# и написать для него по 3-4 теста каждого вида (PyTest, UnitTest, DocTest)
import doctest


class Matrix:
    """
    >>> print(my_matrix)
    1   2   3
    4   5   6
    7   8   9
    >>> print(my_matrix.size())
    (3, 3)
    """
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1]
            string += '\n'
        string = string[:-1]
        return string

    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)
        return (rows, cols)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            length = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != length:
                    raise Exception
            for row2 in other.matrix:
                if len(row2) != length:
                    raise Exception
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise Exception

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * j for j in i] for i in self.matrix]
            return Matrix(result)

    __rmul__ = __mul__

    def are_same(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix)):
                if (self.matrix[i][j] != other.matrix[i][j]):
                    return False
                return True


    def transpose(self):
        trans_matrix = list(zip(*self.matrix))
        self.matrix = trans_matrix
        return Matrix(trans_matrix)

    def transposed(self):
        trans_matrix = list(zip(*self.matrix))
        return Matrix(trans_matrix)


matr1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matr2 = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]

if __name__ == '__main__':
    my_matrix = Matrix(matr1)
    # my_matrix2 = Matrix(matr2)
    print(my_matrix)
    print(my_matrix.size())
    # print(my_matrix.__add__(my_matrix2))  # сложение
    # print(my_matrix.__getitem__(1))
    # print(my_matrix.__mul__(3))  # умножение
    # print(my_matrix.are_same(my_matrix2))  # сравнение
    # print(my_matrix.are_same(my_matrix))

if __name__ == "__main__":
    doctest.testmod(verbose=True)
