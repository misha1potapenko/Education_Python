# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random as rd


def add_in_dict():
    my_dict = {1: (rd.randint(1, 8), rd.randint(1, 8)),
               2: (rd.randint(1, 8), rd.randint(1, 8)),
               3: (rd.randint(1, 8), rd.randint(1, 8)),
               4: (rd.randint(1, 8), rd.randint(1, 8)),
               5: (rd.randint(1, 8), rd.randint(1, 8)),
               6: (rd.randint(1, 8), rd.randint(1, 8)),
               7: (rd.randint(1, 8), rd.randint(1, 8)),
               8: (rd.randint(1, 8), rd.randint(1, 8)), }
    return my_dict


def my_chess():
    while True:
        count = 0
        my_dict = add_in_dict()

        for i in my_dict.values():
            for x in i:
                for j in my_dict.values():
                    if i == j:
                        continue
                    elif x in j:  # Здесь проверка на то что есть ли на линии (столбе) еще один ферзь
                        my_dict = add_in_dict()
                        count = 0
                        continue
                    elif i[0] + i[1] == j[0] + j[1]:  # Здесь проверка диагоналей в одну сторону
                        my_dict = add_in_dict()
                        count = 0
                        continue
                    elif i[0] - i[1] == j[0] - j[1]:  # Здесь проверка диагоналей в другую сторону
                        my_dict = add_in_dict()
                        count = 0
                        continue
                    else:
                        count += 1
                        if count == 40:
                            print(my_dict)
                            return True





my_chess()
print(add_in_dict())