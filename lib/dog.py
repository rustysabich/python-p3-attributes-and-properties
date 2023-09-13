#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    # initialize attribute
    def __init__(self, name='Rex', breed='Pug'):
        self.name = name
        self.breed = breed
        
    # define name as a property
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    # complile the getter and setter methods
    name = property(get_name, set_name)
    
    # define breed as a property
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if (breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            
    # compile the getter and setter methods
    breed = property(get_breed, set_breed)
