# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os
from random import sample
from string import ascii_letters


def creating_folder(number_files: int, extension: str):
    if not os.path.exists('my_dir'):  # создание директории
        os.mkdir('my_dir')
    # создание файлов в директории
    for _ in range(number_files):
        file_name = ''.join(sample(ascii_letters, 5)) + extension  # создание рандомного имени
        demo_path = os.path.join(os.getcwd(), "my_dir", file_name)  #  это создаем путь к файлу

        with open(demo_path, 'w'):
            continue


creating_folder(10, '.txt')


def rename_files(end_name, digits, source_extension, dest_extension, name_range=(0, -1)):
    # Получаем список файлов в текущей директории
    files = os.listdir(os.path.join(os.getcwd(), "my_dir"))

    # Фильтруем только нужные файлы по расширению
    filtered_files = [f for f in files if f.endswith(source_extension)]

    # Пробегаемся по всем файлам
    for i, file in enumerate(filtered_files, 1):
        # Получаем оригинальное имя файла
        # далее описано как работает splitext
        '''Split the pathname path into a pair (root, ext) such that root + ext == path,
         and the extension, ext, is empty or begins with a period and contains at most one period.

If the path contains no extension, ext will be '':

>>>
>>> splitext('bar')
('bar', '')'''
        old_name = os.path.splitext(file)[0][name_range[0]:name_range[1]]

        # Формируем имя файла с указанным окончанием и порядковым номером
        #  Далее описано как работает zfill
        '''Return a copy of the string left filled with ASCII '0' digits to make a string of 
        length width. A leading sign prefix ('+'/'-') is handled by inserting the padding
         after the sign character rather than before. The original string is returned if 
         width is less than or equal to len(s).

For example:

>>>
>>> "42".zfill(5)
'00042'
>>> "-42".zfill(5)
'-0042'''
        new_name = f"{old_name}_{end_name}_{str(i).zfill(digits)}{dest_extension}"

        # Переименовываем файл
        old_path = os.path.join(os.getcwd(), "my_dir", file)
        new_path = os.path.join(os.getcwd(), "my_dir", new_name)
        os.rename(old_path, new_path)


rename_files('new_', 3, '.txt', '.jpg', (0, 3))
