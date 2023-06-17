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

    def show_cash(self):
        return self.cash

    def on_off(self):
        if self.working:
            return ("Банкомат работает")
        else:
            return ("Банкомат не работает")

    def get_money(self):  #здесь нужно создать функцию выдачи денег с карты

        sum_card = int(input("Введите сумму снятия: "))
        if sum_card % 50 == 0:
            if (sum_card * 0.015) > 30:
                my_card.get_money(sum_card + (sum_card * 0.015))
            else:
                my_card.get_money(sum_card + 30)
        else:
            print("Введите сумму кратную 50 ")

    def add_money(self):  #здесь нужно создать функцию добавления денег на карту
        sum_card = int(input("Введите сумму внесения: "))
        my_card.add_money(sum_card)


my_card = Card()   # Создаем экземпляр карты
my_card.set_money(10000)   # создаем баланс карты
my_card.show_money()

new_cash_machine = CashMachine(1_000_000_000, True)
print(new_cash_machine.on_off())
new_cash_machine.get_money()
new_cash_machine.add_money()


