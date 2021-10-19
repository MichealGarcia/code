# Composition

# Inheritance is useful, but another way to do it
# is just to use other classes and modules
# rather than rely on implicit inhereitance.

# Two of three ways of inheritance involve writing new code
# to replace or alter funcitonality.

# This can be replicated by calling functions in a module.

#EXAMPLE:

class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        # calling a method instead of rewriting the code.
        # Isn't this the same as using pass????
        self.other.implicit()
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        # So, instead of calling super()
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# So, did I need to make class Other?

# When to use inheritance or composition

# You don't want duplicated code all over your software.
# It's not clean, or efficient.

# Inheritance solves the problem of reuse, but when is it appropriate?
#   Inheritance is good for implied features set in base classes.

# Composition solves the issue by giving you modules and capability to call functions

# Both solve the problem, but when to use eachother?

# Subjective, but here is an answer.

# 1. Avoid multiple inheritance at all costs, as it's too complex to be
# Reliable. if you're stuck with it, then be prepared to know the class
# hierarchy and spend time finding where everything comes from.

# 2. Use composition to package code into modules that are used in many
# unrelated places and situations.

# 3. Use inheritance only when there are clearly related pieces of code that
# fit under a single concept or if you have to because of something you're using.

