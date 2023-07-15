# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

import math


class Triangle:

    def __new__(cls, *args, **kwargs):
        if len(args) == 3 and Triangle.__exists__(*args):
            obj = super(Triangle, cls).__new__(cls)
            return obj
        else:
            raise Exception("Треугольник не может быть построен на этих сторонах!")

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __exists__(cls, a, b, c):
        return a + b > c and b + c > a and a + c > b and a, b, c > 0

    def info(self):
        print("Стороны: ", self.a, self.b, self.c)

        print("Периметр: ", self.a + self.b + self.c)

        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print("Площадь: ", s)


tr = Triangle(25.0, 10.0, 30)
if tr:
    tr.info()
tr = Triangle(10.0, 10.0, 15)
print('=*' * 43)
if tr:
    tr.info()
