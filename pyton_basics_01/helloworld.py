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


class Car:
    def fuel(self):
        return "Petrol or Diesel"

class ElectricCar:
    def fuel(self):
        return "Electricity"


for vehicle in [Car(), ElectricCar()]:
    print(vehicle.fuel())



print(len("Hello"))  
print(len([1, 2, 3, 4])) 
print(len({"a": 1, "b": 2}))  
