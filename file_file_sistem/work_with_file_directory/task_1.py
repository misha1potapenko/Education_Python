# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random


def fills_in_the_file(file_name: str, count_string: int):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(count_string):
            first_number = random.randint(-1000, 1000)
            second_number = random.uniform(-1000, 1000)
            result = (str(first_number) + '|' + str(second_number) + '\n')
            file = f.write(result)


fills_in_the_file('file.txt', 15)
