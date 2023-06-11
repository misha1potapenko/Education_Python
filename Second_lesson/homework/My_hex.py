# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

my_number = int(input("Введите целое число "))


def do_hex(my_number):
    list_for_hex = []  # Create list for add remainder
    result = 0
    string_for_list = ""
    while my_number > 0:
        result = my_number % 16
        if result == 10:
            list_for_hex.append("A")
        elif result == 11:
            list_for_hex.append("B")
        elif result == 12:
            list_for_hex.append("C")
        elif result == 13:
            list_for_hex.append("D")
        elif result == 14:
            list_for_hex.append("E")
        elif result == 15:
            list_for_hex.append("F")
        list_for_hex.append(result)
        my_number = my_number // 16
        if my_number == 0:
            list_for_hex.reverse()
            print(''.join(str(el) for el in list_for_hex))


do_hex(my_number)
print(hex(my_number))
