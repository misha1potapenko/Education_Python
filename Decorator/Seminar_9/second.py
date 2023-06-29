# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
import random


def outer(func) -> Callable:
    # def wrapper(number: int, attempts: int):
    #     if 0 < number < 101 and attempts<
    #         result = func(number, attempts)
    #
    #     return result

    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
        return func(guess, attempts)

    return wrapper


@outer
def game_guess(num_sc, attempts) -> None:
    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            break
        else:
            advice = ['lesser', 'greater']
            print(f'Your number is {advice[num > num_sc]} then right')
    else:
        print(f'You loose. Right number is {num_sc}')


if __name__ == '__main__':
    game_guess(200, 300)
