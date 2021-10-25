# Most of the uses of inheritane can be simplified or replaced with composition, 
# and multiple inheritance should be avoided at all costs.

# What is inheritance. 
    # Inheritance is used to indicate that one class will
    # get one or all of its features from a parent class.

        # There are 3 ways that the parent and child classes can interact.
            # Actions on the child imply an action on the parent.
            # Actions on the child override the action on the parent
            # Actions on the child alter the action on the planet.

#EXAMPLES

    #IMPLICIT INHERITANCE

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()

son = Child()

dad.implicit()
son.implicit()

# Using pass in the Child class is saying that it will inherit all
# of its behaviour from Parent class.



