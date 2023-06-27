import os
import shutil
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
# os.chdir('../..')   # изменение дирректории
# print(os.getcwd())
# print(Path.cwd())


file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
# здесь список файлов и директорий
print(os.listdir())
# здесь перебор путей
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)

# ● Проверка на директорию, файл и ссылку
# Получив информацию о содержимом текущего каталога зачастую требуется
# уточнить что перед нами. В каталогах можно хранить другие каталоги и файлы. В
# файлах содержатся данные. А символьные ссылки указывают на каталоги и файлы
# из других мест.
# Рассмотрим варианты получения информации об объектах, полученных в примере
# кода выше.


dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')
p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')

# ● Обход папок через os.walk()
# Функция os.walk рекурсивно обходит каталоги от переданного в качестве аргумента
# до самого нижнего уровня вложенности.

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
# Функция возвращает кортеж из трёх значений:
# ➢ dir_path — абсолютный путь до каталога
# ➢ dir_names — список с названиями всех каталогов, находящихся в dir_path

# переименование файлов
os.rename('old_name.py', 'new_name.py')
p = Path('old_file.py')
p.rename('new_file.py')
Path('new_file.py').rename('newest_file.py')

# перемещение файлов
os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

 # копирование файла

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')

#  копирование каталога
shutil.copytree('dir', 'one_more_dir')