# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
import logging
import time
from typing import Callable
from datetime import datetime


def main(func: Callable):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='decorator_log.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
        logging.debug(f'Запуск функции {func.__name__} в {datetime.now()}')
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        logging.info(f'Результат функции {func.__name__}: {result} с аргументом {args}')
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper


@main
def my_factorial(number: int):
    if number == 1:
        return 1
    else:
        return number * my_factorial(number - 1)


print(f'Factorial = {my_factorial(8)}')
