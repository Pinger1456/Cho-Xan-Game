"""Cho-Han, by Al Sweigart al@inventwithpython.com
    The traditional Japanese dice game of even-odd.
    Tags: short, beginner, game"""

import random
import sys
from player import Player


class Game:
    """Main instructions for the game"""

    JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                        4: "SHI", 5: 'GO', 6: 'ROKU'
                        }

    def __init__(self):
        self.player = Player()

    @staticmethod
    def roll():
        """Giving random values from 1-6 for Dice1 and Dice2"""
        return random.randint(1, 6)

    def play_round(self):
        """Place your bet:"""
        print('You have', self.player.get_balance(),
              'mon. How much do you bet? (or QUIT)')

        while True:
            pot = input('> ')
            if pot.upper() == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            elif not pot.isdecimal():
                print('Please enter a number.')
            else:
                # This is a valid bet.
                # Convert pot to an integer.
                pot = int(pot)
                try:
                    self.player.place_bet(pot)
                    # Exit the loop once a valid bet is placed.
                    break
                except ValueError as e:
                    print(e)

        # Roll the dice.
        dice1 = self.roll()
        dice2 = self.roll()

        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks for your bet.')
        print()
        print('    CHO (even) or HAN (odd)?')

        # Reveal the dice results:
        print('The dealer lifts the cup to reveal:')
        print('  ', self.JAPANESE_NUMBERS[dice1], '-',
              self.JAPANESE_NUMBERS[dice2])
        print('    ', dice1, '-', dice2)

        # Determine if the player won:
        roll_is_even = (dice1 + dice2) % 2 == 0
        correct_bet = 'CHO' if roll_is_even else 'HAN'

        # Let the player bet cho or han:
        while True:
            bet = input('> ').upper()
            if bet not in ('CHO', 'HAN'):
                print('Please enter either "CHO" or "HAN".')
            else:
                break

        player_won = bet == correct_bet

        # Display the bet results:
        if player_won:
            print('You won! You take', pot, 'mon.')
            # Add the pot from player's balance.
            self.player.balance = self.player.balance + pot
            print('The house collects a', pot // 10, 'mon fee.')
            # The house fee is 10%.
            self.player.balance = self.player.balance - (pot // 10)
        else:
            # Subtract the pot from player's balance.
            self.player.balance = self.player.balance - pot
            print('You lost!')

        # Check if the player has run out of money:
        if self.player.get_balance() == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()

    def start(self):
        """by Al Sweigart al@inventwithpython.com"""

        print('''Cho-Han.
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.''')

        while True:
            self.play_round()
