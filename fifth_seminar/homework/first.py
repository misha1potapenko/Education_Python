# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# ✔Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int, премия str с
# указанием процентов вида «10.25%». В результате получаем словарь с
# именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).


# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# import os
# from os import path
#
# p = os.path.abspath('first.py')
# print(p)
#
#
# name = os.path.basename(r'C:\python3\file.txt ')
# print(name)
#
#
# full_name = path.basename(r'C:\python3\file.tar.gz ')
# name = path.splitext(full_name)[1]
# print(name)


def abs_path(abs_path: str) -> tuple:
    result = []
    result.append(abs_path)
    for_result = abs_path.split('\\')
    result.append(for_result[-1])
    for_result2 = for_result[-1].split('.')
    result.append(for_result2[-1])
    return tuple(result)


my_string = r"C:\Users\misha\PycharmProjects\Education_Python\fifth_seminar\homework\first.py"


print(abs_path(my_string))
