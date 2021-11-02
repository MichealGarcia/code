#Cocktail making game, you get a list of recipes.
#Starting at level 1, the drinks will be two step drinks (two ingredients, then add ice)
# Level 2: 3 step
# level 4: 4 step
# Will get harder with each level.


# Making drinks
    # cocktail, has a name and a recipe
    # gets ordered
    # ingredients are combined by measurements
    # shaken or stirred?
    # glassware?
    # garnish?

from sys import exit
from random import randint
from textwrap import dedent

class Cocktail(object):

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty


class Game(object):

    def level1(self):

        print("Your first order is coming in!")
        print("_"*10)

    def level2(self):

        print("New orders are coming in!")
        print("_"*10)

    def level3(self):

        print("Last round of orders for the night, get ready!")
        print("_"*10)

old_fashioned = Cocktail("Old Fashioned", 2)
game = Game()
game.level1()










