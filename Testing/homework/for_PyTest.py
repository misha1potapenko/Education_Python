import pytest
from matrix import Matrix


matr1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matr2 = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]


def test_are_same():
    first_matrix = Matrix(matr1)
    second_matrix = Matrix(matr2)
    assert first_matrix.are_same(first_matrix), 'Матрицы не равны'


if __name__ == '__main__':
    pytest.main()
