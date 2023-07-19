import unittest
from matrix import Matrix


matr1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matr2 = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]


class TestCaseName(unittest.TestCase):
    first_matrix = Matrix(matr1)
    second_matrix = Matrix(matr2)

    def test_method(self):

        self.assertFalse(self.first_matrix.are_same(self.second_matrix))
        self.assertTrue(self.first_matrix.are_same(self.first_matrix))

    def test_for_size(self):
        self.assertEqual(self.first_matrix.size(), (3, 3), msg='Размер не верен')

if __name__ == '__main__':
    unittest.main()
