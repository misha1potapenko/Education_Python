# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Square:
    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def square(self):
        return self.length * self.width

    def perimetr(self):
        return (self.length + self.width) * 2


square1 = Square(2)


print(square1.square())
print(square1.perimetr())

