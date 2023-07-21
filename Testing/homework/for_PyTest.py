import pytest
from matrix import Matrix


matr1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matr2 = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]




def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


if __name__ == '__main__':
    pytest.main()
