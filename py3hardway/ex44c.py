# Alter before or after

# This way you alter the behaviour before or after the Parent class version runs.
# Using the built-in super fumction to the the parent version to call.

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

