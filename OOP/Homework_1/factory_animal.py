from animal import Dog, Fish, Bird


class Factory:
    """ Класс для создания животных"""

    def __init__(self):
        choice = input('Введите какого животного вы хотите создать '
                       'Dog, Fish, Bird  ')
        if choice == 'Dog':
            self.dog = Dog()
        elif choice == 'Fish':
            self.fish = Fish()
        elif choice == 'Bird':
            self.bird = Bird()
        else:
            print('Мы не можем создать такое животное, попробуйте еще раз')


    def __str__(self):
        return f'{Dog} {Fish} {Bird}'


factory1 = Factory()
print(factory1)
