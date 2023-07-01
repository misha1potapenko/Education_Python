import os


print(os.getcwd())   # Показывает текущую директорию

print(os.getcwd().split('\\')[-1:])  # при помощи среза берем директорию в которой мы работаем

os.path.exists('sample_data') # проверка существует ли такая директория
