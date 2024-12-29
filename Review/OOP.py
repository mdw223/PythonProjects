class Cat:
    def __init__(self, name, age, breed, sex):
        self.name = name
        self.age = age
        self.breed = breed
        self.sex = sex
    
    def __str__(self): # use \ backslash to continue on the next line
        return f"My cat's name is {self.name} and is {self.age} years.\
              It is a {self.sex} and is a {self.breed}."
    
    def purr(self):
        print("purrrrrr")

citty = Cat("Kinder", 4, "Siamese", 'Female')
citty.purr()
print(citty) # My cat's name is Kinder and is 4 years. It is...