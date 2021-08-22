import os
import sys


class Animal:
    # __ is used to define private variables. That means to change or get the values of these we need functions
    __height = 0
    __weight = 0
    __sound = ""

    # Constructor - to setup of initialize the object
    def __init__(self, name, weight, height, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # Encapsulation - restricting and validating data before setting values
    # self allows the object to refer it self inside of the class (same like this)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return str( self.__height )

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return str( self.__weight )

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    # Polymorphism

    def get_type(self):
        print( "Animal" )

    def to_string(self):
        return "{} is {} cm tall {} kg and says {}".format( self.__name, self.__height, self.__weight, self.__sound )


cat = Animal( "Whiskers", 33, 10, "Meow" )
print( cat.to_string() )


# Inheritance
class Dog( Animal ):
    __owner = ""

    def __init__(self, name, weight, height, sound, owner):
        self.__owner = owner
        super( Dog, self ).__init__( name, weight, height, sound )

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print( "Dog" )

    # method overriding
    def to_string(self):
        return f"{self.get_name()} is {self.get_height()} cm tall {self.get_weight()} kg and says {self.get_sound()}. " \
                f"His owner is {self.get_owner()} "

    # method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print( self.get_sound() )
        else:
            print( self.get_sound() * how_many )


spot = Dog( "Spot", 53, 27, "Ruff", "John" )
print( spot.to_string() )


# Polymorphism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type( cat )
test_animals.get_type( spot )
spot.multiple_sounds( 4 )
spot.multiple_sounds()
