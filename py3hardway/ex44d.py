# Mix of all inheritacne examples

class Parent(object):

    def override(self):
        print("PARENT implicit()")

    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
#Create instance of dad with class Parent
dad = Parent()
# Create instance of son with class Child
son = Child()

#with dad call implicit with param self
dad.implicit()
# with son call implicit with param self, this is overrided by calss Parent
# because class Child does not have a behaviour implicit
son.implicit()

# with dad call function override()
dad.override()
# with son call function override, which is explicitly different than PArent class
son.override()

# with dad call function altered and get initial behaviour
dad.altered()
# With son call altered and get an overridden behaviour and calss Parent behaviour.
son.altered()

