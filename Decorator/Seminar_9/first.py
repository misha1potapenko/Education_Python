# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
import random


def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = random.randint(0, 100)
            print(result)
            for _ in range(num):
                if result > func(*args, **kwargs):
                    print('Введите число больше')
                elif result < func(*args, **kwargs):
                    print('Введите число меньше')
                else:
                    print("Yes")
                    break

            return result

        return wrapper

    return deco


@count(10)
def guess():
    my_guess = int(input("Введите число от 0 до 100  "))
    return my_guess


print(guess())


# from typing import Callable
# from random import randint
#
#
# def outer() -> Callable:
#     num_range = int(input('Input number 1 -- 100: '))
#     attempts = int(input('Input number of attempts (1 -- 10): '))
#     num_sc = randint(1, num_range)
#
#     def inner() -> None:
#         nonlocal num_range, attempts
#         while attempts:
#             print(f'left {attempts} attempts.', end=' ')
#             attempts -= 1
#             num = int(input('Input a number: '))
#             if num == num_sc:
#                 print(f'Number found: {num}')
#                 break
#             else:
#                 advice = ['lesser', 'greater']
#                 print(f'Your number is {advice[num > num_sc]} then right')
#         else:
#             print(f'You loose. Right number is {num_sc}')
#     return inner
#
#
# def main():
#     game = outer()
#     game()
#
#
# if __name__ == '__main__':
#     main()
