from collections import defaultdict


class Storage:

    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


# s = Storage()
# print(s(42))
# print(s(72))
# print(s('Hello world!'))
# print(s(0))
# print(s)

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first < self.stop:
                return self.first
        raise StopIteration


#
# fib = Fibonacci(20, 100)
# for num in fib:
#     print(num)

import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)

        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


# db = DB('sqlite.db')
# with db as cur:
#     cur.execute("""create table if not exists users(name, age);""")
#     cur.execute("""insert into users values ('Гвидо', 66);""")


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > self._age:

            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')

    @age.deleter
    def age(self):
        self._age = 0


# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошёл один год.')
# user.age = 76
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
# user.age = 25  # ValueError: Новый возраст должен быть больше текущего: 76


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age},grade={self.grade}, office={self.office})'


if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    std_other = Student('Аристотель', 2406, 5, 17)  # ValueError:Значение 2406 должно быть меньше 103
    print(f'{std_one = }')
    std_one.age = 15
    print(f'{std_one = }')
    std_one.grade = 11.0  # TypeError: Значение 11.0 должно быть целым числом
    std_one.office = 73  # ValueError: Значение 73 должно быть  меньше 42
    del std_one.age  # AttributeError: Свойство "_age" нельзя удалять
    print(f'{std_one.__dict__ = }')
