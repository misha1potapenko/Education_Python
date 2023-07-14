import csv


class City:
    def __init__(self, row, header):
        self.__dict__ = dict(zip(header, row))

    def __str__(self):
        return f' {list(map(self.__dict__))}'


data = list(csv.reader(open('file.csv')))
instances = [City(i, data[0]) for i in data[1:]]

print(list(instances))

import csv

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
            # Вывод строк
            print(f'    {row[0]} - {row[1]} оценки по предмету {row[2]}')
        count += 1
    print(f'Всего в файле {count} строк.')

my_str = "ddsdsshfgdcest"
split(my_str)