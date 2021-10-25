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

# class Meeting(object):

#     def __init__(self):
#         self.handshake = True
#         self.hello = True
#         self.ignore = False
#         self.possible_interaction = True

#     def shake_hand(self, handshake):
#         if handshake == True:
#             self.shake_hand_intro()
#         else:
#             handshake = True
#             self.shake_hand(handshake)

#     def say_hello(self, hello):
#         if hello == True:
#             self.hello_intro()
#         else:
#             hello = True
#             self.say_hello(hello)
    
#     def ignore_stranger(self, ignore):
#         if ignore == True:
#             self.no_interaction()
#         else:
#             ignore = True
#             self.ignore_stranger(ignore)
    
#     def shake_hand_intro(self):
#         print("**You shake hands and introduce yourselves.**")


class Human(object):

    def __init__(self):
        self.human = True
        self.exists = True
        self.name = ""
        self.job = ""
        self.age = ""
        self.description = []
        self.introduced = False

    def persona(self):
        describe = self.description
        describe.append(input("Name?:\n"))
        describe.append(input("Job?:\n"))
        describe.append(input("Age?:\n"))
        self.name = describe[0]
        self.job = describe[1]
        self.age = describe[2]

    def existence(self):
        if self.exists == True:
            self.persona()
        else:
            print("It appears you don't exist, goodbye.")
            sys.exit()
    
    def introduction(self):



    def friend(self, introduction):
        if 

            
    



class You(Human):
    pass

class Stranger(Human):
    pass
    


you = You()
jeff = Stranger()
jeff.exists = True
#print attribute to see if you exist. Debug
#print(you.exists)you.exists = False

#Prove you exist by describing yourself
you.existence()
jeff.existence()
friendship1 = you.friends(you, jeff)
print(you.description)
print(you.name)
print(you.age)
print(you.job)
print(jeff.age)

print(friendship1)






# Stopping coding, reviewing current work

# I think I will restart, and create humans as my main object. 

# Class Human
    # has-a __init__ attributes: name, job, age
    # has-a introduction
    # has-a persona
    # has-a existence

# You is-a Human
# Stranger is-a Human
    # has-a not_introduced
# Friend is-a Human
    # has-a introduced