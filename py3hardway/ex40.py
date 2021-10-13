# Moving onto classes!!!! I think that understanding Objects and Classes will be huge for my ability to code

# Basics of OOP (Object-Orient Programming)

# 4 pillars of OOP
    # Abstraction, Inheritance, Polymorphism, Encapsulation
    # OOP is a paradigm based on objects
        # Objects can contain data in form of attributes/properties
        # and actions in form of functions and methods
    
    # Abstraction
        # To only show the necessary details to the user of the object.
        # Coding example:
            # Say you have an object for enemies and they have attributes like
            # health and to say something. You can go to your main script and call
            # the talk method.
        
    # Inheritance
        # Allows code reusability
        # Coding example:
            # You want to build a new class derived from an existing class.
            # This would create a subclass and the original would be the parent class
            # Say you want to make a specific enemy, a vampire, using our enemy class
            # And if you want to override a specific attribute, you can give it own
            # talk or health method.
    
    # Polymorphism
        # Most advanced topic
        # Allows what type of function to run while code is running
        # Coding example:
            # We make a Werewolf class, and go back to the main class
            # We call both vampire and werewolf, subclasses of enemy class,
            # Werewolf and Vampire are sibling classes.
            # If we point at a specific sublass for enemy mother class,the Spoiler in Batman Eternal
            # We can make an array with all sublcasses and the enemy class will call child objects.

    # Encapsulation
        # Built on the idea of data hiding
        # You can make a class private, and then it wont change the property
        # of an object.
        # (So instead you will use setter and getter functions. 
        # *This part is not a definition.)


mystuff = {'apple': "I AM APPLES"}
print(mystuff['apple'])

# Say this file is called mystuff.py
def apple():
    print("I AM APPLES")

# import mystuff
# mystuff.apple()
# ^ This would call the function from the mystuff module

# then create a variable inside the module

tangerine = "Living reflectin of a dream"

#This can be accessed the same way as apple()
# mystuff.tangerine

#So far we have a few different ways to grab data from objects.

# first example is dictionary: mystuff['apple']
# second is module method: mystuff.apple()
# this is variable: mystuff.tangerine

# Here is the common patterm
    # Take a key=value style container
    # get something out of it using the key

# Classes are like modules.
# think of modules as a special dictionary that hold python code,
# which can be called using the . operator.

class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("I AM CLASSY APPLES!")

# This is a mini module. With an apple function in it.
# You use classes instead of modules because you can use them to
# create several more of them. *confusing for now

# So we need to understand what an object is.

thing = Mystuff()
thing.apple()
print(thing.tangerine)

# Calling a class as a variable, and instantiate object.
    # python does a sequence of events for you behind the scenes.
        # 1. Python looks for Mystuff() and sees a class you defined
        # 2. Python crafts an object with all the functions you've specified in the class with def.
        # 3. Python then looks to see if you have a "magic" __init__ function.
            # __init__, it is used to initialize your new empty object.
        # 4. In the Mystuff function __init__ there is an extra variable, self.
            # self, is the empty object python made for us.
            # self, can have variables set on it.
        # 5. Inthis case I set self.tangerine to a song lyric and initialized this object
        # 6. Now python can take the newly created object and assign it to the thing variable to work with.

# This is a "mini-import" when you call a class like a function.
# So this is not giving you the class, but using the class as a blueprint.

# This is slightly inaccurate idea of ho these work,
# The truth is that classes and objects suddenly diverge from modules at this point.

# more honest explanation
    # Classes are like blueprints or definitions for creating new mini-modules
    # Instatiation ishow you make one of these mini-modules and import at the same time.
    # "Instantiate" means to create an object from a class.
    # The resulting created mini-module is called an object, and you then assign it to a variable to work with it.

# This is just the basics


# So earlier we realized there are 3 ways to get things from things.
# Classes : thing = Mystuff()
# methods/modules : thing.apples()
# attributes from variables: print(thing.tangerine)

# Our first Class

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With a pocket ful of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


# Importance of self and __init__
    # If you don't have self, then code like cheese = 'Frank' is ambiguous.
    # That code isn't clear about whether you mean the instance's cheese attribute
    # or a local variable named cheese.
    # With self.cheese = 'Frank' it is very clear you mean the instance attribute self.cheese.

