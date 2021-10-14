## Animal is-a object
class Animal(object):
    pass

## Class Dog is-a Animal, an object of animal, it has-a init
## that takes param self and name
class Dog(Animal):

    def __init__(self, name):
        ## the dog has-a name
        self.name = name

## Class Cat is-a Animal, object of Animal, it has-a init that takes
## self and name as params
class Cat(Animal):

    def __init__(self, name):
        ## The Cat has-a name
        self.name = name

## class Person is-a object, that has-a init that takes self and name params
## Person has-a name
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet
        self.pet = None

##class Employee is-a person that has-a init that takes self, name, salary params
class Employee(Person):

    def __init__(self, name, salary):
        ## new thing, unsure what it is
        ## my guess is that it is calling a function with params Employee and self
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## create a class Fish that is-a object.
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Mary")

## mary is a person
mary = Person("Mary")

## with mary get attribute pet that is satan
## stan is pet of mary
mary.pet = satan

## set frank as an instance of Employee with name Frank, 120000 param
frank = Employee("Frank", 120000)

## with frank get attribute pet that is rover
## frank has a pet rover
frank.pet = rover

## set flipper as an instance of Fish
flipper = Fish()

## set crouse as an instance of Salmon
crouse = Salmon()

## set harry as an instance of Halibut
harry = Halibut()



