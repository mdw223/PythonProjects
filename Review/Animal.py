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

class Human(Animal):
    number_of_kids = 0
    number_of_humans = 0

    def __init__(self, name, age, nationality):
        super().__init__(name, age) # calls the super to initalize 
        self.nationality = nationality
        Human.add_human()
    
    def sound(self):
        return f"Hello my name is {self.name}."
    
    def add_kid(cls): # use cls to call a class variable or method
        cls.number_of_kids += 1

    def get_number_of_kids(cls):
        return cls.number_of_kids
    
    def str_number_of_kids(cls):
        return f"The number of kids I have is {str(cls.number_of_kids)}"
    
    # must add to make it so when called, it is not specific to a certain instance, 
    # rather it is specific to the class Human, so it allows us to get the sum of total humans 
    @classmethod 
    def add_human(cls):
        cls.number_of_humans += 1
    
    @classmethod
    def get_number_of_humans(cls):
        return cls.number_of_humans
    
    ## this is a static method, not required like above to add a @ but i will
    @staticmethod
    def total_humans(cls):
        print(f"The total number of humans is {str(cls.get_number_of_humans())}")
    
human = Human("Bill", 50, "American")
print(human.sound())
human.add_kid()
print(human.str_number_of_kids())
human_1 = Human("Joe", 55, "Brit")
print(human_1.sound())
human_1.add_kid()
human_1.add_kid()
human_1.add_kid()
print(human_1.str_number_of_kids())
human.total_humans()





