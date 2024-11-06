"""Cho-Han, by Al Sweigart al@inventwithpython.com
    The traditional Japanese dice game of even-odd.
    Tags: short, beginner, game"""


class Player:
    """Introducing current balance of Player"""
    def __init__(self, balance=5000):
        self.balance = balance

    def place_bet(self, amount):
        """Analyzing input()"""
        if amount > self.balance:
            raise ValueError('Not enough money for bet')
        self.balance -= amount
        return amount

    def add_winnings(self, amount):
        """If won - You Won! + Cash"""
        self.balance += amount

    def get_balance(self):
        """Just giving your present Balance"""
        return self.balance
