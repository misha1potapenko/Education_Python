class Value:

    def init(self, min_value):
        self.min_value = min_value

    def set_name(self, owner, name):  # length widht
        self.param_name = '_' + name

    def get(self, instance, owner):
        return getattr(instance, self.param_name)

    def set(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def delete(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')


class Square:
    # slots = ["_length", "_widht"]
    _length = Value(1)
    _widht = Value(1)

    def init(self, a, b=None):

        self._length = a
        if b:

            self._widht = b
        else:

            self._widht = a

    @property
    def length(self):
        return self._length

    @property
    def wight(self):
        return self._widht

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError

    @wight.setter
    def wight(self, value):
        if value > 0:
            self._widht = value
        else:
            raise ValueError

    def square(self):
        return self._length * self._widht

    def perimeter(self):
        return 2 * (self._length + self._widht)


sq = Square(1, -2)  # Дискриптор работает только при создании
print(sq.square())
print(sq.perimeter())
sq.length = -5
print(sq.square())
print(sq.perimeter())

sq.size = 20
print(sq.size)