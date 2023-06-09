# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import datetime


class MyString(str):
    """Строка документации для класса моя строка, который дополнительно хранит имя строки и время создания"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

    def __main__(self):
        return """Строка документации для класса моя строка, который дополнительно хранит имя строки и время создания"""

    def __str__(self):
        return f'Имя - {self.name}  Дата - {self.date}'

first_string = MyString('dsdsdsds', 'autor')
print(first_string.date)

str_st = MyString("sdsd", "dsds")
print(str_st)
# help(MyString)
