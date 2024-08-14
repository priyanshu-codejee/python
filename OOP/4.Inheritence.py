class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(Self):
        print("I am Eating")

myanimal = Animal()

myanimal.eat()
myanimal.who_am_i()

# This class is going to funaction as a base class and other classes may inherit some of the ,ethods from this class.
# Suppose I want to make a DOG class which has many methods common to both.

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # We can overwrite any method of base class for a particular derived class
    def who_am_i(self):
        print("I am a dog")

    # We can also add new methods in derived class.
    def bark(self):
        print("Woof!")

    def eat(Self):
        print("I am Eating and i am a dog")

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()