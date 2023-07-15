class UserException(Exception):
    pass


class ProblemSideTriangle(UserException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Возраст пользователя должен быть целым int() или вещественным float() больше нуля.\n' \
                f'У вас тип {type(self.value)}, а значение{self.value}'


class UserNameError(UserException):
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = 'попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.lower:
            text = 'больше верхней'
            return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов).\n' \
                    f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'

