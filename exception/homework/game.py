# определение пользовательских исключений
class Error(Exception):
    """Базовый класс для других исключений"""
    pass

class ValueTooSmallError(Error):
    """Вызывается, когда входное значение мало"""
    pass

class ValueTooLargeError(Error):
    """Вызывается, когда входное значение велико"""
    pass

# число, которое нужно угадать
number = 10

# игра продолжается до тех пор,
# пока пользователь его не угадает
while True:
    try:
        i_num = int(input("Ввести число: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Это число меньше загаданного, попробуйте еще раз!\n")
    except ValueTooLargeError:
        print("Это число больше загаданного, попробуйте еще раз!\n")

print("Поздравляю! Вы правильно угадали.")