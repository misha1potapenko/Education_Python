# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import random
import csv
import cmath
from typing import Callable

def find_sqrt(a: int, b: int, c: int):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print(f'The solution are {sol1} and {sol2}')


# функция для записи csv файла


def csv_writer():
    with open('number_for_decorator.csv', 'a', newline='') as csvfile:
        writer_csv = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(100, 1000):
            list_for_csv = [i for i in range(1, 100)]
            random.shuffle(list_for_csv)   # перемешиваем список
            csv_list = random.sample(list_for_csv, k=3)  # выбираем здесь три случайных числа из списка
            writer_csv.writerow(csv_list)


def csv_reader():
    with open('number_for_decorator.csv', newline='') as csvfile:
        reader_csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
        when_stop = random.randint(1, 900)   # с какой строчки взять 3 числа
        count = 0
        for row in reader_csv:
            count += 1
            if count == when_stop:
                return row


def main(func: Callable):
    def wrapper(*args, **kwargs):
        csv_writer()
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        return result
    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
        return f


print(f'{factorial(1000) = }')
control = main(factorial)
print(f'{control.__name__ = }')
print(f'{control(1000) = }')