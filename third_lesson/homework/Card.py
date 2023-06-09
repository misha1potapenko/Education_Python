class Card:

    def __init__(self, money):
        self.money = money

    def get_money(self, sum_for_get_money): #Создаем функцию выдачи денег с карты
        return (self.money - sum_for_get_money)
