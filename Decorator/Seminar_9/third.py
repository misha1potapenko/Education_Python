# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
import os
from typing import Callable
import random


def outer(file_name) -> Callable:
    def inner_func(func):
        def wrapper(*args, **kwargs):
            my_dict = {func(*args, **kwargs): [arg for arg in args] + [(key, value) for key, value in kwargs.items()]}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            return func(*args, **kwargs)
        return wrapper
    return inner_func


@outer('file.json')
def function_json(*args, **kwargs) -> str:
    list_for_args = []
    list_kwargs = []
    if args:
        for i in args:
            list_for_args.append(i)
    if kwargs:
        for key, value in kwargs.items():
            list_kwargs.append(f'{key}={value}')
    result_str = ' '.join(list(map(str, list_for_args))) + ' '.join(list(map(str, list_kwargs)))

    return result_str




if __name__ == '__main__':
    print(function_json(1, 2, 3, 4, 5, 6))
    print(function_json(tex=1,
                        te=2,
                        dsfsdf=3))
