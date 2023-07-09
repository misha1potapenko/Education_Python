from animal import Dog, Fish, Bird


class Factory:
    """ Класс для создания животных"""

    def __init__(self, name):
        self.name = name

    def add_animal(self):
        while True:
            choice = input('Введите какого животного вы хотите создать '
                           'Dog, Fish, Bird  ')
            if choice == 'Dog':
                name = input('Введите имя собаки  ')
                dog = Dog(name)
                print(dog.name)
                return dog
            elif choice == 'Fish':
                name = input('Введите имя рыбки  ')
                fish = Fish(name)
                print(fish.name)
                return fish
            elif choice == 'Bird':
                name = input('Введите имя птички  ')
                bird = Bird(name)
                print(bird.name)
                return bird
            else:
                print('Мы не можем создать такое животное, попробуйте еще раз')


factory1 = Factory('first')
print(factory1.add_animal())
