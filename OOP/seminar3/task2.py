# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
from collections import defaultdict


class MyGenarator:


    def __init__(self, *args):
        start, stop, step, result = 1, 1, 1, 1
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
        elif len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        else:
            raise AttributeError

        if start < stop:
            self.start = start
            self.stop = stop
            self.step = step
            self.result = result
            self.iter_step = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.result *= (self.start + self.step * self.iter_step)

        if self.start + self.step * self.iter_step >= self.stop:
            raise StopIteration
        self.iter_step += 1
        return self.result


my_gener = MyGenarator(10, 51, 10)
for i in my_gener:
    print(i)
