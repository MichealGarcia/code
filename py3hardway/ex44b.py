# Override Explicitly
# Sometimes you want the Child class to behave differently
class Parent(object):

    def override(self):
        print("PARENT override()")

    def voice(self):
        print("I am the Father")

    son_favorite_food = "Taco's"
        
class Child(Parent):

    def override(self):
        print("CHILD override()")

    def voice(self):
        print("I am his son")
    
    son_favorite_food = "Pizza"

dad = Parent()
son = Child()

dad.override()
son.override()

print("What is your son's favorite food?")

print(f"Dad: {dad.son_favorite_food}")
print(f"Son: ...{son.son_favorite_food}")



