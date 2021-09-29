
def start():
    
    print(f"""\n\n\t\t\tWelcome to my game!

\t   This is a game that will always end the same.
\t       But there is only one way to beat it.


\t\t  Life is about the journey and I 
\t      hope you enjoy yours in this wonderful 
\t\t\t little adventure\n\n\n\n\n\n\n\n""")
    #Starting hill
    print("You have suddenly appeared on top of a large, but walkable, hilltop.")
    print("You can go in any of the four cardinal directions.")
    
    look = input("n, e, s, or w?\n>").lower()
    
    if look[0] == "n":
        forest()
    elif look[0] == "e":
        hills()
    elif look[0] == "s":
        cave()
    elif look[0] == "w":
        lake()
    else:
        print("try again")
        try_again("Four cardinal directions...")


#forest
def forest():

    print("The forest is dense.")
    print("\n\nThere is a pond to the left and a bear den to the right")
    answer = input("left or right?\n\n\n>")

    if answer[0] == "r":
        #bear den
        bear_den()
    if answer[0] == "l":
        #magic_pond
        magic_pond()

def bear_den():

    print("You find yourself outside of a bear den.")
    print("try to look inside?")
    peek = input("Yes or No?\n>")

    if peek[0] == "y":
        bear_encounter()
        
    elif peek[0] == "n":
        print("Yeah, its probably rude to look inside someones home.")
        go_back = input("Maybe we should go to the pond?\n Yes or No?\n>")

def bear_encounter():
    print('A bear appears suddenly, and exclaims, "Not cool, that\'s my home.\nAnd you were planning to invade my privacy like that?\nMaybe I should just walk into YOUR home, eat your porridge."\n')
    print('*The bear stares at you with dissapointment\n\n')
    print("You ignore that the bear was talking and go towards the pond.")

start()
