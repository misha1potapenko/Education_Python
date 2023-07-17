class UserException(Exception):
    pass


class ProblemSideTriangle(UserException):
    def __init__(self, *args):
        self.value = args

    def __str__(self):
        return f'Вы не можете создать треугольник с такими сторонами {self.args}\n'


class UserNameError(UserException):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        text = 'попадает в'
        if self.a + self.b < self.c:
            text = 'Side is bad'
        elif len(self.name) > self.lower:
            text = 'больше верхней'
            return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов).\n' \
                    f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'

