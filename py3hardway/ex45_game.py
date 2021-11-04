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



# Another idea: Create instance for every item used.
    # Spirits(object)
    # Mixer(object)
    # Glassware(object)

from sys import exit
from random import randint
from textwrap import dedent

class Cocktail(object):

    def __init__(self, name, difficulty, ingredients):
        self.name = name
        self.difficulty = difficulty
        self.ingredients = ingredients

class Game(object):

    def level1(self, cocktail_list):

        print("Your first order is coming in!")
        print("_"*10,"\n")
        print(dedent(f"""
                    {cocktail_list[0]}
                    {cocktail_list[1]}
                    {cocktail_list[2]}
                    """))
        print("_"*10,"\n")

    def level2(self, cocktail_list):

        print("New orders are coming in!")
        print(dedent(f"""
                    {cocktail_list[0]}
                    {cocktail_list[1]}
                    {cocktail_list[2]}
                    """))
        print("_"*10,"\n")

    def level3(self, cocktail_list):

        print("Last round of orders for the night, get ready!")
        print(dedent(f"""
                    {cocktail_list[0]}
                    {cocktail_list[1]}
                    {cocktail_list[2]}
                    """))
        print("_"*10,"\n")
    
    def cocktail_list(self, cocktail1, cocktail2, cocktail3):
        list_of_cocktails = [cocktail1, cocktail2, cocktail3]
        return list_of_cocktails

    def play(self, cocktails):
        print(cocktails)
        ready = input("press any key to start")
        if ready:
            pass

        



gin_tonic = Cocktail("Gin & Tonic", 1, 
                                            {
                                            "Gin": "2oz",
                                            "Tonic": "3oz"
                                            })
seven_seven = Cocktail("7 & 7", 1, 
                                            {
                                            "Seagram's 7": "2oz",
                                            "Sprite": "3oz"
                                            })
rum_coke = Cocktail("Rum & Coke", 1,
                                            {
                                            "Rum": "2oz",
                                            "Coke": "3oz"
                                            })
old_fashioned = Cocktail("Old Fashioned", 2, 
                                            {
                                            "Whiskey": "2oz",
                                            "Simple Syrup": ".25oz",
                                            "Angostura Bitters": "3 Dashes"
                                            })
lemon_drop = Cocktail("Lemon Drop", 2, 
                                            {
                                            "Vodka": "2oz",
                                            "Lemon Juice": ".75oz",
                                            "Triple Sec": ".75oz"
                                            })
sazerac = Cocktail("Sazerac", 2, 
                                            {
                                            "Whiskey": "2oz",
                                            "Simple Syrup": ".25oz",
                                            "Peychaud's Bitters": "3 Dashes"
                                            })                                         

game = Game()
list_of_cocktails1 = game.cocktail_list(gin_tonic.name, seven_seven.name, rum_coke.name)
list_of_cocktails2 = game.cocktail_list(old_fashioned.name, lemon_drop.name, sazerac.name)













