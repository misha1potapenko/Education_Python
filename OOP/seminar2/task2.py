# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Строка документации для класса архив, который хранит пару свойств и сохраняет в список свойства"""
    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'



new_ex = Archive('hsjdhs', 1)
help(new_ex)

