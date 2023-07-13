# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def number():
    while True:
        try:
            num = input('Inter an integer:')
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError as e:
            print('You introduced not number')



number()