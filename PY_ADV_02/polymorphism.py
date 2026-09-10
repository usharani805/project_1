class Dog:
    def sound(self):
        print("Dog says: Woof Woof")


class Cat:
    def sound(self):
        print("Cat says: Meow")


class Cow:
    def sound(self):
        print("Cow says: Moo")


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Polymorphism
animals = [dog, cat, cow]

for animal in animals:
    animal.sound()