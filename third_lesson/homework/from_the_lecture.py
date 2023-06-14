# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


my_dict = {'Иван': ('фонарь', 'котелок', 'палатка', 'нож', 'ложка'),
           'Петр': ('спички', 'вода', 'тушенка', 'гречка', 'ложка'),
           'Николай': ('котелок', 'мангал', 'палатка', 'удочки', 'чай'), }


def backpack_capacity(my_dict: dict):
    for y in my_dict.values():
        print(f" {y}")


backpack_capacity(my_dict)