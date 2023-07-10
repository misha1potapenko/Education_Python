# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
from collections import defaultdict


class Factorial:

    def __init__(self):
        self.storage = defaultdict(list)

    def __call__(self, value):
        factorial = 1
        for i in range(2, value+1):
            factorial *= i
        return factorial
