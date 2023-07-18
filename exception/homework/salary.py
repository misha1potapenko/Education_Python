class SalaryNotInRangeError(Exception):
    """Исключение возникает из-за ошибок в зарплате.

    Атрибуты:
        salary: входная зарплата, вызвавшая ошибку
        message: объяснение ошибки
    """

    def __init__(self, salary, message="Зарплата не входит в диапазон (5000, 15000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    # переопределяем метод '__str__'
    def __str__(self):
        return f'{self.salary} -> {self.message}'

salary = int(input("Введите сумму зарплаты: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)