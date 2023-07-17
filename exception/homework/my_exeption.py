class UserException(Exception):
    pass


class ProblemSideTriangle(UserException):
    def __init__(self, *args):
        self.value = args

    def __str__(self):
        return f'Вы не можете создать треугольник с такими сторонами {self.args}\n'




