class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " Says Woof!"
    
    
class Cat():

    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " Speaks Meow!"
    

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())
    

for pet in [niko,felix]:

    print(type(pet))
    print(pet.speak())




# Abstract class: Never instantiated, It on;y serves as a base class. 
class Animal():

    def __init__(self,name):
        self.name = name
    
    def speak(Self):
        raise NotImplementedError("Subclass must inmplement this abstrac t method")
    
'''
myanimal = Animal('Ferd')
myanimal.speak()

NOt to be used like this.
'''

class Dog(Animal):
    def speak(self):
        return self.name+ " says woof!"
    
class Cat(Animal):
    def speak(self):
        return self.name+ " speaks meow!"