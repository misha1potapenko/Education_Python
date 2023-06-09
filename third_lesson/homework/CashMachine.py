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

    def __init__(self, cash, working):
        self.cash = cash
        self.working = working

    my_card = Card(10000)

    def show_cash(self):
        return self.cash

    def on_off(self):
        if self.working:
            return ("Банкомат работает")
        else:
            return ("Банкомат не работает")

    def get_money(self, my_card):
        my_card = Card(10000)
        return (mycard.)




new_cash_machine = Cash_machine(1000000, True)
print(new_cash_machine.on_off())



