# Base class: Animal
class Animal:
    def move(self):
        return "The animal moves."

# Subclass: Dog
class Dog(Animal):
    def move(self):
        return "The dog runs."

# Subclass: Bird
class Bird(Animal):
    def move(self):
        return "The bird flies."

# Subclass: Fish
class Fish(Animal):
    def move(self):
        return "The fish swims."

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())