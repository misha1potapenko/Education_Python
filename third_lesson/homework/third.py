# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

my_dict = {'котелок': 0.4,
           'вода': 1.2,
           'палатка': 3.2,
           'ложка': 0.2,
           'ножик': 0.3,
           'фонарик': 0.7, }


def backpack_capacity(my_dict: dict, load_capacity):
    load = 0
    for y, x in my_dict.items():
        load += x
        if load < load_capacity:
            print(y)


backpack_capacity(my_dict, 2)
