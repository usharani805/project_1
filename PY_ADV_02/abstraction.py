from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")


# Child class
class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof Woof")


# Child class
class Cat(Animal):

    def make_sound(self):
        print("Cat says: Meow")


# Creating objects
dog = Dog()
cat = Cat()

# Calling methods
print("Dog:")
dog.make_sound()
dog.sleep()

print("\nCat:")
cat.make_sound()
cat.sleep()