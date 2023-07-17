# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

import math
from my_exeption import ProblemSideTriangle


class Triangle:

    def __new__(cls, *args, **kwargs):
        if len(args) == 3 and Triangle.__exists__(*args):
            obj = super(Triangle, cls).__new__(cls)
            return obj
        else:
            raise ProblemSideTriangle

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __exists__(cls, a, b, c):
        if (a + b > c and b + c > a and a + c > b) and (a, b, c > 0):
            return True
        else:
            raise ProblemSideTriangle

    def info(self):
        print("Стороны: ", self.a, self.b, self.c)

        print("Периметр: ", self.a + self.b + self.c)

        p = (self.a + self.b + self.c) / 2
        try:
            s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        except ProblemSideTriangle as p:
            print(p)
        print("Площадь: ", s)


if __name__ == '__main__':
    tr = Triangle(25, 10.0, 30)
    tr.__exists__(0, 10.0, 30)
    if tr:
        tr.info()
    tr = Triangle(10.0, 10.0, 15)
    print('=*' * 43)
    if tr:
        tr.info()
