class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)

dog = Animal("dog","mammals",17)
print(dog)