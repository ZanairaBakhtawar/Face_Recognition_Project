class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())



class Bird:
    def fly(self):
        return "Can fly"

class Penguin:
    def fly(self):
        return "Cannot fly"

# Polymorphism in action
for animal in [Bird(), Penguin()]:
    print(animal.fly())
