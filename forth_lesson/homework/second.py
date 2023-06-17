# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def my_kwargs(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")

my_kwargs("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

