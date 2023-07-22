# Первое задание
# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день
# недели, текущий день недели и/или текущий месяц.
# 📌 Научите функцию распознавать не только текстовое названия дня недели
# и месяца, но и числовые, т.е не мая, а 5.
# []
# Второе задание
# 📌 Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse


def abs_path(abs_path: str) -> tuple:
    result = []
    result.append(abs_path)
    for_result = abs_path.split('\\')
    result.append(for_result[-1])
    for_result2 = for_result[-1].split('.')
    result.append(for_result2[-1])
    logging.basicConfig(filename='Path.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
    logging.info(str(result))
    return tuple(result)


my_string = r"C:\Users\misha\PycharmProjects\Education_Python\fifth_seminar\homework\first.py"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер для определения пути к файлу, файла и его расширения')
    parser.add_argument('path', metavar='path for file', type=str, nargs='+', help='Enter path')
    args = parser.parse_args()
    print(abs_path(*args.path))
