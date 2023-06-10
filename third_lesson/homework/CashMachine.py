# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
from Card import Card


class CashMachine:

    'Класс банкомат с некотрыми полями и функциями'

    my_card = Card(10000)


    def __init__(self, cash, working):
        self.cash = cash
        self.working = working

    def show_cash(self):
        return self.cash

    def on_off(self):
        if self.working:
            return ("Банкомат работает")
        else:
            return ("Банкомат не работает")

    def get_money(self, my_card):  #здесь нужно создать функцию выдачи денег с карты
        sum_get = int(input("Введите сумму выдачи: "))

        return print(f"Остаток на счете: {my_card.money - sum_get}")


my_card = Card(10000)
new_cash_machine = CashMachine(1000000, True)
print(new_cash_machine.on_off())
print(new_cash_machine.get_money(my_card))


