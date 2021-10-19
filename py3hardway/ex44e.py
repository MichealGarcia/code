# The reason for Super()

# This is where trouble can happen
# You can get something called multiple inheritance, when
# you define a class that inherits from more than one class
    # EXAMPLE:
        #class superFun(Child, BadStuff):
            #pass

    #---> This is like saying,
        # Make a class named superFun that inherits from the classes,
        # child and BadStuff at the same time.

# Using the Super Function does this for you but handles the placement
# of functions in a fancy organized way, that I do not understand.

# the most common use of super() is in __init__

#EX
    # def __init__(self, stuff):
        #self.stuff = stuff

    #---> This is pretty much the same as Child.altered used earlier, except
    # we set variables inthe __init__ before having the parent initialize with its
    # Parent.__init__


