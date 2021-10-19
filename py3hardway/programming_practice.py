# This is using PEP 8 guidelines to create habit in skills to program efficiently

# This will house the main focus of the code
class Main(object):
    
    # has-a __init__ (init represents the instance object itself) ---> foo = Main()
    def __init__(self):
        self.x = 'Hello'

    # has-a function first_method that takes self, and bar params
    def first_method(self, text):
        # print the attribute self.x with a space and then any text param
        print(self.x + ' ' + text)

class Human(object):

    # Human attributes, basic level
    def __init__(self):
        self.head = True
        self.left_arm = True
        self.right_arm = True
        self.left_leg = True
        self.right_leg = True
        self.words = "Hello there."
        self.name = ""
    
    def speak(self, text):
        print(text)

class You(Main):

    def __init__(self):
        super(You, self).__init__()
        self.name = input("My name is. >>>")
    pass

class Stranger(Human):
# Align the parameters equally to first delimiter.
    def intro(self, name, 
              height, age, health):
        
        print(f"""
        I am {name}. My height is {height},
        and I am {age} years old. I am in
        {health} health.\n\n""")
    
    def avoid(self):
        print("*This stranger avoids you entirely")

    pass
class Friend(Human):
    
    def stranger_to_friend(introduced):
        if introduced == True:
            print("We are friends now")
    pass
start = You()
name_start = start.name
stranger1 = Stranger()

start.first_method("there.")
stranger1.intro("Bob", "5' 10",
          "27", "okay")

stranger2 = Stranger()

stranger2.avoid()




