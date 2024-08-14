class Dog():

    #Class Object Attribute which are same for any instance of a class.
    species = "Mammal"

    def __init__(self,breed,name,spots):  
        ''' 
        init is a constructor for a class, 
        Self creates an instance of the class and helps to refer to itself.
        Slef keyword is automatically defind while creating a class in other languages but in python we have to explicitly define it.
        '''

        # Atrribute            
        # We take in the arguement
        # we assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #Expect T/F
        self.spots = spots

my_dog = Dog(breed = 'Lab', name = 'sammy', spots = False)
print(type(my_dog.breed))
print(type(my_dog.name))
print(type(my_dog.spots))
print(type(my_dog.species))