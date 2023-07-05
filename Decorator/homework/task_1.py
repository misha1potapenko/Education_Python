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


# import complex math module
import csv
# import cmath
#
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
#
# # calculate the discriminant
# d = (b ** 2) - (4 * a * c)
#
# # find two solutions
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# print('The solution are {0} and {1}'.format(sol1, sol2))
import random

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
        for row in reader_csv:
            print(', '.join(row))

csv_writer()