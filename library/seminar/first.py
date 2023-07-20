# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging
import random
from datetime import datetime


def not_zero():
    number = int(input('Input number = '))
    if number == 0:
        logging.basicConfig(filename='log.log', filemode='a', encoding='utf-8', level=logging.INFO)
        logging.error('Input number = 0' ' ZeroDivisionError: division by zero')
        current_now = datetime.now()
        logging.info(current_now)
    result = random.randint(1, 100)/number
    return result
not_zero()