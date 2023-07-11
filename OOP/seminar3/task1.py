# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
import json
from collections import defaultdict


class Factorial:

    def __init__(self):
        self.results = defaultdict(list)


    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.results[number].append(result)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items()))
        return txt

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        new_file = open("manager_file.json", "w", encoding="utf-8")
        json.dump(self.results, new_file, indent=4, ensure_ascii=False)
        new_file.close()

factor = Factorial()

factor(1)
factor(10)
factor(3)
factor(2)

print(factor)
with factor as new_file:
    new_file(10)


# factor = Factorial()
#
# factor(1)
# factor(10)
# factor(6)
#
# print(factor)


