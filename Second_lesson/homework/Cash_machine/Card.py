class Card:

    def __init__(self):
        self.money = 0

    def show_money(self):
        """Show how money in card"""
        print(f"In card: {self.money}")

    def set_money(self, set_money):
        """ Set balance in card"""
        self.money = set_money


    def add_money(self, set_money):
        """ Set balance in card"""
        self.money += set_money
        print(self.money)

    def get_money(self, set_money):
        """ Set balance in card"""
        self.money -= set_money
        print(self.money)



