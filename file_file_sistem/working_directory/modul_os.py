import os


print(os.getcwd())   # Показывает текущую директорию

print(os.getcwd().split('\\')[-1:])  # при помощи среза берем директорию в которой мы работаем

print(os.path.exists('new_data'))  # проверка существует ли такая директория

if not os.path.exists('test_dir'):  # создание директории
    os.mkdir('test_dir')
    os.makedirs(os.path.join('test_dir1', 'level_1', 'level_2', 'level_3'))  # так создают вложенные директори

print(os.listdir())  #  показывает содержимое каталога

# for root, dirs, files in os.walk('C:\\Users\\misha\\PycharmProjects\\Education_Python\\file_file_sistem'):
#     print(root)                                              # показывает содержимое каталога и подкаталогов
#     print(dirs)
#     print(files)


