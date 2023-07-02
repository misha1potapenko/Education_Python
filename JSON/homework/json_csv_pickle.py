# Напишите функцию, которая получает на вход директорию
# # и рекурсивно обходит её и все вложенные директории.
# # Результаты обхода сохраните в файлы json, csv и pickle.
# # []
# # ○Для дочерних объектов указывайте родительскую директорию.
# # ○Для каждого объекта укажите файл это или директория.
# # ○Для файлов сохраните его размер в байтах, а для директорий
# # размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
from os.path import join, getsize

def walk_in_directory(file_path):
    for root, dirs, files in os.walk(file_path):
        print(f'Это директория(и) {dirs}', end="\n")
        print(f'Это файл(ы) {files}', end="\n")
        print(root, "consumes", end="\n")
        demo_path = os.path.join(os.getcwd(), file_path)
        print(demo_path)
        # print(sum(getsize(join(root, name)) for name in files), end=" ")
        # print("bytes in", len(files), "non-directory files")
        # if 'CVS' in dirs:
        #     # не просматриваем каталог `CVS`
        #     dirs.remove('CVS')


walk_in_directory('C:\\Users\\misha\\PycharmProjects\\Education_Python\\JSON')