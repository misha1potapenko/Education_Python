# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

class Descriptor:
    def __init__(self):
        self.__surname = ""

    def __get__(self, instance, owner):
        return self.__surname

    def __set__(self, instance, value):
        if isinstance(value, str) and value.istitle():
            print(value)
        else:
            raise TypeError("A string must be entered here with the first letter capitalized")

        if len(value) == 0:
            raise ValueError("The string can not be empty ")

        self.__surname = value

    def __delete__(self, instance):
        del self.__surname


class Car:
    surname = Descriptor()
    name = Descriptor()
    patronymic = Descriptor()

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} '


car2 = Car("Dfdfd", "Dsdfsdfsd")
print(car2)
# 40
# BMW model X7 with a fuel capacity of 40 ltr.
