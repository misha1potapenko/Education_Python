# Напишите функцию, которая получает на вход директорию
# # и рекурсивно обходит её и все вложенные директории.
# # Результаты обхода сохраните в файлы json, csv и pickle.
# # []
# # ○Для дочерних объектов указывайте родительскую директорию.
# # ○Для каждого объекта укажите файл это или директория.
# # ○Для файлов сохраните его размер в байтах, а для директорий
# # размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import os
from os.path import join, getsize


def walk_in_directory(file_path):
    for root, dirs, files in os.walk(file_path):
        folder = root.split('\\')
        print(f'В директории {folder[-1]}', end="\n")
        if not dirs:
            print("В этой папке нет директорий")
        else:

            print(f'Директория(и) {dirs}', end="\n")
        print(f'Файл(ы) {files}', end="\n")
        # print(f' В директории {root}', end="\n")

        print(sum(getsize(join(root, name)) for name in files), end="\n")

        to_json = {'trunk': trunk_template, 'access': access_template}

        with open('sw_templates.json', 'w') as f:
            json.dump(to_json, f)


        # print("bytes in", len(files), "non-directory files")
        # if 'CVS' in dirs:
        #     # не просматриваем каталог `CVS`
        #     dirs.remove('CVS')


walk_in_directory('C:\\Users\\misha\\PycharmProjects\\Education_Python\\JSON')


import json

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json, f)

with open('sw_templates.json') as f:
    print(f.read())