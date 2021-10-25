# This is using PEP 8 guidelines to create habit in skills to program efficiently

# This practice script will take objects and have them interact. Specifically, the main class is a meeting between you, and a stranger.

# when people meet they interact, or they ignore.
# Attributes of meeting include -> greetings like shaking hands or hello, an introduction and description of self.  
#Meeting
    #attributes: shake_hand, hello, ignore
    #methods: shake_hand_intro, hello_intro, no_interaction
# Human
# You
# Stranger
# friend



# This will house the main focus of the code

import sys

class Meeting(object):

    def __init__(self):
        self.handshake = True
        self.hello = True
        self.ignore = False
        self.possible_interaction = True

    def shake_hand(self, handshake):
        if handshake == True:
            self.shake_hand_intro()
        else:
            handshake = True
            self.shake_hand(handshake)

    def say_hello(self, hello):
        if hello == True:
            self.hello_intro()
        else:
            hello = True
            self.say_hello(hello)
    
    def ignore_stranger(self, ignore):
        if ignore == True:
            self.no_interaction()
        else:
            ignore = True
            self.ignore_stranger(ignore)
    
    def shake_hand_intro(self):
        print("**You shake hands and introduce yourselves.**")


class Human(object):

    def __init__(self):
        self.human = True
        self.exists = True
        self.name = ""
        self.job = ""
        self.age = ""
        self.description = []

    def persona(self):
        d = self.description
        self.name = d.append(input("What's your name?:\n"))
        self.job = d.append(input("What do you do?:\n"))
        self.age = d.append(input("How old are you?:\n"))


class You(Human):
    pass

class Stranger(Human):

    def __init__(self):
        self.seems_rude = False
    pass

class Friend(Human):

    def __init__(self):
        self.introduced = True
    pass
    


you = You()

#print attribute to see if you exist. Debug
#print(you.exists)you.exists = False

#Prove you exist by describing yourself
if you.exists == True:

    you.persona()

else:
    print("It appears you don't exist, goodbye.")
    sys.exit()

print(you.description)






