import sys
import time
from intro import *
from termcolor import *
import os


# Intro 
def hit_enter():

    text = colored('Hit enter', 'red', attrs=['bold', 'blink'])

    prompt = input(f"\t\t\t     {text}")



def begin():
    opening()
    hit_enter()
begin()


def start():
    items = []
    #Starting hill
    print("You have suddenly appeared on top of a large, but walkable, hilltop.")
    print("You can go in any of the four cardinal directions.")
    
    look = input("n, e, s, or w?\n>").lower()
    
    if look == "":
        print("Please enter a direction")
        start()
    elif look[0] == "n":
        forest()
    elif look[0] == "e":
        hills()
    elif look[0] == "s":
        cave()
    elif look[0] == "w":
        lake()
    else:
        print("There are only four cardinal directions.")
        start()

def forest():

    print("The forest is dense.")
    print("\n\nThere is a pond to the left and a bear den to the right")
    answer = input("left or right?\n\n\n>")

    if answer[0] == "r":
        #bear den
        bear_den()
    elif answer[0] == "l":
        #magic_pond
        magic_pond()
    else:
        print("left or right")
        forest()


def bear_den():

    print("You find yourself outside of a bear den.")
    print("try to look inside?")
    peek = input("Yes or No?\n>")

    if peek[0] == "y":
        bear_encounter()
        
    elif peek[0] == "n":
        print("Yeah, its probably rude to look inside someones home.")
        go_back = input("Maybe I should go to the pond?\nYes or No?\n>").lower()
        if go_back[0] == "y":
            magic_pond()
        else:
            bear_encounter2()



def bear_encounter():
    print('A bear appears suddenly, and exclaims, "Not cool, that\'s my home.\nAnd you were planning to invade my privacy like that?\nMaybe I should just walk into YOUR home, eat your porridge."\n')
    print('*The bear stares at you with dissapointment\n\n')
    print("You ignore that the bear was talking and go towards the pond.")
    print("The bear starts crying dramatically, and starts to talk about how nobody ever acknowledges that it talks.")
    door_shut()
    magic_pond()
def bear_encounter2():
    print("A bear suddenly appears behind you.")
    print("The bear says, \"hello.\"")
    response = input("Respond? Yes or no?\n>").lower()
    if response[0] == "y":
        print("You compliment the bears ability to talk, saying \"wow, a talking bear.\"")
        print("The just sits down and everything goes black.")
        print("When you come too you are standing facing a small pond, the path to the bear den is gone.")
        magic_pond()
    elif response[0] == "n":
        print('*The bear stares at you with dissapointment\n\n')
        print("You ignore that the bear was talking and go towards the pond.")
        print("The bear starts crying dramatically, and starts to talk about how nobody ever acknowledges that it talks.")



        
    
        acknowledge = input("Acknowledge the bears ability to talk? Yes or No?\n>").lower()

        if acknowledge[0] == "y":
            print("You compliment the bears ability to talk, saying \"wow, a talking bear.\"")
            print("The just sits down and everything goes black.")
            print("When you come too you are standing facing a small pond, the path to the bear den is gone.")
            magic_pond()
        else:  
            print("The bear still looks to yo with dissapointment.")
            print("You start walking to the pond")
            door_shut()
            magic_pond()
def door_shut():
    print("As you start to leave the area, you hear the sound of a door shut behind you.")




def magic_pond():
    print("As you get loser to the pond, you hear soft giggling.")
    print("Call out to the giggle?")
    call_out = input("Yes/No\n>").lower()
    if call_out[0] == "y":
        print("You call out to the empty area.")
        fairy_bad_timing()
    elif call_out[0] == "n": 
        print("You kneel down to look into the lake")
        fairy_bad_timing()
    else:
        print("Les's try again :)")
        magic_pond()

#fairy interaction
def fairy_bad_timing():
    print("Suddenly! Three fairies appear on each of your shoulders and one atop your head.")
    print("They dare you to touch the water.")
    touch = input("Touch the water? Yes or No?\n>").lower()
    if touch[0] == "y":
        knowledge()
    elif touch[0] == "n":
        print("The ground is wet and slippery")
        print("You slip and fall into the water.")
        return_home("pond")
        
        
    else:
        print("Seriously? Yes or No?")
        fairy_bad_timing()

def knowledge():
    print("As you reach towards the water, the fairies start giggling.")
    print("But there is no turning back because thats too much programming and this was the right decision.")

    return return_home("pond")

def return_home(location):
    if location == "pond":
        print("The fairies combine into a figure, but you can't make out who it is.")
        start()
    elif location == "island":
        print("")


start()