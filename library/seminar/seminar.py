# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату

# 📌Напишите программу, которая использует модуль logging
# для вывода сообщения об ошибке в файл. 📌
# Например отлавливаем ошибку деления на ноль.
# import logging
# import random
#
#
# def by_zero():
#     number = int(input('Введите целое число'))
#     if number == 0:
#         logging.basicConfig(filename='for_log.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
#         logging.info('ZeroDivisionError: division by zero')
#     for_number = random.randint(1, 100) / number
#     return for_number
#
# by_zero()


# 📌На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# 📌Напишите аналогичный декоратор, но внутри используйте модуль logging.
# 📌Доработаем задачу 2. 📌Сохраняйте в лог файл раздельно: ○уровень логирования,
# ○дату события, ○имя функции (не декоратора), ○аргументы вызова, ○результат.
# import logging
# import time
# from typing import Callable
from datetime import datetime


#
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         logging.basicConfig(filename='log_factorial.log', filemode='a', encoding='utf-8',
#                             level=logging.DEBUG)
#         my_datetime = datetime.now()
#         logging.info(f'Запуск функции {func.__name__} c  аргументом {args} дата {my_datetime}')
#         result = func(*args, **kwargs)
#         logging.info(f'Результат функции {func.__name__}: {result}')
#         logging.info(f'Завершение функции {func.__name__}')
#         return result
#     return wrapper
#
#
# @main
# def my_factorial(number: int):
#     if number == 1:
#         return 1
#     else:
#         return number * my_factorial(number-1)
#
# print(my_factorial(8))

# 📌Функция получает на вход текст вида:
# “1-й четверг ноября”, “3я сре мая” и т.п.
# 📌Преобразуйте его в дату в текущем году.
# 📌Логируйте ошибки, если текст не соответсвует формату.

def my_date(str_date: str):
    parse_date = str_date.split()
    dict_for_day = {'пон': 'Monday', 'вто': 'Tuesday', 'сре': 'Wednesday',
                    'чет': 'Thursday', 'пят': 'Friday', 'суб': 'Saturday', 'вос': 'Sunday'}
    dict_for_month = {
        'янв': 'January', 'фев': 'February', 'мар': 'March', 'апр': 'April',
        'мая': 'May', 'июн': 'June', 'июл': 'July', 'авг': 'August',
        'сен': 'September', 'окт': 'October', 'ноя': 'November', 'дек': 'December'}
    if parse_date[1][:3] in dict_for_day:
        date_day = dict_for_day[parse_date[1][:3]]
    if parse_date[2][:3] in dict_for_month:
        month = dict_for_month[parse_date[2][:3]]
    day = parse_date[0][:1]
    string_date = date_day + " " + month + " " + "2023"

    text_date = datetime.strptime(string_date, '%A %B %Y')
    print(text_date)


my_date('3я среда мая')
