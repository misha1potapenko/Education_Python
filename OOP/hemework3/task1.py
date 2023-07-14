# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv


class Descriptor:
    def __init__(self):
        self.__surname = ""

    def __get__(self, instance, owner):
        return self.__surname

    def __set__(self, instance, value):
        if isinstance(value, str) and value.istitle():
            print("\t")
        else:
            raise TypeError("Вы ввели что-то непонятное, должны быть введены ФИО начиная каждое слово с"
                            " большой буквы и без цифр")

        if len(value) == 0:
            raise ValueError("The string can not be empty ")

        self.__surname = value

    def __delete__(self, instance):
        del self.__surname


class Student:
    surname = Descriptor()
    name = Descriptor()
    patronymic = Descriptor()

    def __init__(self, surname, name, patronymic, file_name):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.file_name = file_name

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} '

    @staticmethod
    def get_mark():
        with open("file.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:

                if count == 0:
                    # Вывод строки, содержащей заголовки для столбцов
                    print(f'Файл содержит столбцы: {", ".join(row)}')
                else:
                    sum_for_mark = sum(list(map(int, (char for char in row[2])))) + \
                                   sum(list(map(int, (char for char in row[3]))))
                    len_for_mark = len((list(char for char in row[2]))) + len((list(char for char in row[3])))
                    # Вывод строк
                    for i in (list(char for char in row[2])):
                        if not (2 <= int(i) <= 5):
                            print(f' Оценка - {i} не действительна  по предмету {row[1]}')
                    for i in (list(char for char in row[3])):
                        if not (2 <= int(i) <= 5):
                            print(f' Оценка - {i} не действительна  по предмету {row[1]}')
                    print(f'    {row[0]} - {row[1]} оценки по предмету {row[2]} оценки по тестам {row[3]} \n'
                          f' средний бал по предмету {row[1]}'
                          f' {sum(list(map(int, (char for char in row[2])))) / len((list(char for char in row[2])))}')
                count += 1
            print(f' средний бал по всем предметам и тестам {sum_for_mark/len_for_mark}')
            print(f'Всего в файле {count} строк.')


Student2 = Student("Petrov", "Ivan", "Fedorovich", "file.csv")
print(Student2)
Student2.get_mark()
