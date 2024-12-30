from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def sound():
        pass # subclasses will implement this 
    
class Dog(Animal): # inheritance
    def sound(self):
        return "woof"
    # When you define a method in a class, it operates on a specific instance of that class. 
    # The self parameter gives the method a way to refer to the attributes and other methods of that specific instance.

    
class Cat(Animal):
    def sound(self):
        return "meow"
    
dog = Dog("spot", 1)
cat = Cat("Kits", 3)
print(dog.sound())
print(cat.sound())
