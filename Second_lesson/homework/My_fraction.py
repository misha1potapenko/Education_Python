# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def my_multiplication():
    fract1 = input("Input first fraction ")
    fract2 = input(("Input second fraction "))
    numerator1 = fract1.split("/")  # разобьем на числитель и знаменатель в список
    numerator2 = fract2.split("/")

    numerator = int(numerator1[0]) * int(numerator2[0])
    denumerator = int(numerator1[1]) * int(numerator2[1])

    if (numerator % 2 == 0) and (denumerator % 2 == 0):
        numerator = numerator/2
        denumerator = denumerator/2
    if (numerator % 2 == 0) and (denumerator % 2 == 0):
        numerator = numerator/2
        denumerator = denumerator/2
    if (numerator % 3 == 0) and (denumerator % 3 == 0):
        numerator = numerator/3
        denumerator = denumerator/3
    if (numerator % 7 == 0) and (denumerator % 7 == 0):
        numerator = numerator/7
        denumerator = denumerator/7

    print(f"Умножение {int(numerator)}/{int(denumerator)}")

    total = Fraction(fract1) * Fraction(fract2)
    print(f"Проверка {total}")


my_fractions()

def my_sum():
    fract1 = input("Input first fraction ")
    fract2 = input(("Input second fraction "))
    numerator1 = fract1.split("/")  # разобьем на числитель и знаменатель в список
    numerator2 = fract2.split("/")

    if numerator1[1] == numerator2[1]:     # Если знаменатели равны
        numerator = int(numerator1[0]) + int(numerator2[0])
        denumerator = int(numerator1[1])

    if (numerator % 2 == 0) and (denumerator % 2 == 0):
        numerator = numerator/2
        denumerator = denumerator/2
    if (numerator % 2 == 0) and (denumerator % 2 == 0):
        numerator = numerator/2
        denumerator = denumerator/2
    if (numerator % 3 == 0) and (denumerator % 3 == 0):
        numerator = numerator/3
        denumerator = denumerator/3
    if (numerator % 7 == 0) and (denumerator % 7 == 0):
        numerator = numerator/7
        denumerator = denumerator/7

    print(f"Умножение {int(numerator)}/{int(denumerator)}")

    total = Fraction(fract1) + Fraction(fract2)
    print(f"Проверка {total}")
