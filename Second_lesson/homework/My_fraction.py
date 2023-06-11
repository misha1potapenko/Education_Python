# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
fract1 = input("Input first fraction ")
fract2 = input(("Input second fraction "))
total = Fraction(fract1) * Fraction(fract2)
print(total)
