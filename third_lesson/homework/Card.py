class Card:

    def __init__(self, money):
        self.money = money

    def get_money(self, sum_for_get_money):
        return (self.money - sum_for_get_money)
