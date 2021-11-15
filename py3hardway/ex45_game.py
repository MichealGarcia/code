# Cocktail making game, cocktails have different difficulties determined by amount of
# ingredients. Each level has three drinks (for now), pulled from a dictionary.
# Each cocktail has a name, ingredients, and measurements.
# There is an intro level that makes you pour a shot of Fernet Branca.
# The game will only have 3 levels to start.
# When a level starts, a ticket will print with orders of cocktail names
# these cocktails will appear one at a time when you confirm that you are ready to start.
# When you start, you will get text saying make me a {cocktail_name}.
# Then you will type the first ingredient, the second, third, and fourth


# Code in a check recipe book, So to start game, either look at recipe book or start.


class Game(object):

    def start(self):
        pass

class Engine(object):
    total_points = 0
    points = 0
    
    def __init__(self, cocktail_objects_list):
        self.cocktail_objects_list = cocktail_objects_list

    def guess_the_spirit_ingredient(self):
        points = 0
        total_points = 0
        for object in self.cocktail_objects_list:
            if object.tier == 1:

                print(f"Drink order: {object.ingredients_dict['Name']}")
                guess_spirit = str(input("what is the main spirit?\n")).lower()
                
                if guess_spirit == object.ingredients_dict["Spirit"].lower():
                    points+=1
                    total_points+=1
                else:
                    print("Incorrect")
                    points=points
                    total_points+=1

                guess_ingredient = str(input("What is the mixer?\n")).lower()

                if guess_ingredient == object.ingredients_dict['Mixers'].lower():
                    points+=1
                    total_points+=1
                else:
                    print("Incorrect")
                    points=points
                    total_points+=1
            
            elif object.tier == 2 or object.tier == 3:
                
                print(f"Drink order: {object.ingredients_dict['Name']}")
                guess_spirit = str(input("What is the main spirit?\n")).lower()

                if guess_spirit == object.ingredients_dict['Spirit'].lower():
                    points+=1
                    total_points+=1
                else:
                    print("Bug or typo")
                    points=points
                    total_points+=1


                for ingredients in object.ingredients_dict['Mixers']:

                    ingredients = ingredients.lower()
                    guess_ingredient = str(input("What is a mixer in this cocktail?\n")).lower()
                    if guess_ingredient in object.ingredients_dict['Mixers']:
                        points+=1
                        total_points+=1
                    else:
                        print("Incorrect")
                        points=points
                        total_points+=1


                    

                
        
        print(f"Debugger: {points}/{total_points}")

    def test(self):
        for object in self.cocktail_objects_list:
            print(object.ingredients_dict["Name"])



class Cocktail(object):

    def __init__(self, tier, ingredients_dict):

        self.tier = tier
        self.ingredients_dict = ingredients_dict





gin_tonic = Cocktail(1,
                        {"Name": "Gin and Tonic",
                        "Spirit": "Gin",
                        "Mixers": "tonic"
                        })
seven_seven = Cocktail(1,
                        {"Name": "7 & 7",
                        "Spirit": "Whiskey",
                        "Mixers": "sprite"
                        })
rum_coke = Cocktail(1,
                        {"Name": "Rum & Coke",
                        "Spirit": "Rum",
                        "Mixers": "coke"
                        })
old_fashioned = Cocktail(2,
                            {"Name": "Old Fashioned",
                            "Spirit": "Whiskey",
                            "Mixers": ["simple syrup", "angostura bitters"]
                            })
lemon_drop = Cocktail(2,
                        {"Name": "Lemon Drop",
                        "Spirit": "Vodka",
                        "Mixers": ["triple sec", "lemon juice"]
                        })
sidecar = Cocktail(2,
                    {"Name": "Sidecar",
                    "Spirit": "Cognac",
                    "Mixers": ["triple sec", "lemon juice"]
                    })
sazerac = Cocktail(3, 
                    {"Name": "Sazerac",
                    "Spirit": "Whiskey",
                    "Mixers": ['simple syrup', 'absinthe', 'peychaud\'s bitters']
                    })
last_word = Cocktail(3, 
                        {"Name": "Last Word",
                        "Spirit": "Gin",
                        "Mixers": ['green chartreuse', 'lime juice', 'luxardo']
                        })                        
whiskey_sour = Cocktail(3, 
                        {"Name": "Whiskey Sour",
                        "Spirit": "Whiskey",
                        "Mixers": ["simple syrup", "lemon juice", "egg white"]
                        })

cocktail_list = [gin_tonic, seven_seven, rum_coke, old_fashioned, lemon_drop, sidecar, sazerac, last_word, whiskey_sour]

engine = Engine(cocktail_list)

engine.guess_the_spirit_ingredient()
#engine.test()











