# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:

    """Класс сложения, сравнения матриц с методами вывода на печать"""
    def __init__(self, matrix):
        self.matrix = matrix[list]


    def __str__(self):
        for i in len(self.matrix):
            print(i)

