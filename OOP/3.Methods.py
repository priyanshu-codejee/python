class Dog():
    
    species = "Mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    # Operation/Actions ---> Method (Method is a function which is within a class)

    def bark(self,number):
        print("Woof! My name is {} and the numeber is {}".format(self.name,number)) 
        # self.number not written because it is user provided and is not an instance of the object.


my_dog = Dog('Lab','Frankie')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.species)

my_dog.bark(10)



class Circle():

    # Class Object Attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = self.pi*radius**2
        # Self.Area = Circle.pi*radius**2  --> This can also be written.

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
