#how to comment 

# from os import path
# import numpy as np
'''
msg = "The dog bites"
print(msg)
print("So never come back")

print(np.random.randint(1,9)) ''' 

# printing hello world 
print("Hello World")
# can also use '
print('Hello World')

# type()
print(type("hello"))

# string concatination
print("Hello" + " World")
# , concatinates string, adding a space
s1 = "String 1" # variables don't need their type to be specified 
s2 = "String 2"
print(s1, s2)

# math operations
print(5 // 2 ) # quotient
print(5 % 2) # mod gives remainder
print (5**2) # exponent 

t = True
f = False
print(not t) # ! is not 
print(3 != 2)  # equality operators
print(3 == 2)

# if statenebt
if t:
    print("if statement worked")

# dictionary (array/list)

phone_1 = "iphone"
phone_2 = 'samsung'

phone_list = [phone_1, phone_2]
print(phone_list)

#appending to a list
phone_list.append("Moto g")
print(phone_list)

#for each loop 
print("\n")
for item in phone_list:
    print(item)
print(len(phone_list)) # len() to get size of a string or obj
print(phone_list[2]) # get a specific element in dictionary

for i in [0, 1, 2, 3]:
    print(i)

for i in [0, 1, 2]:
    print(phone_list[i])

print("\n") # new line 
# range is the same as an array not including inside the params
for i in range(3):  
    print(phone_list[i])
for i in range(len(phone_list)):  
    print(phone_list[i])

''' list() iterates through its parameter and puts each instance 
in an array to output it '''
print(list(range(len(phone_list)))) 

''' enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

'''
print(enumerate(phone_list))
for i, item in enumerate(phone_list):
    print(i, item)

b = 5
while(b >= 0): # while loop
    print(b)
    b -= 1 # decrement 

if 5 > 3:
    print('true1') # elif, this is printed in this series of ifs
elif 5 > 4:
    print('true2')
elif 5 > 5:
    print('true3')
else:
    print('false')

print(True or False) # similar to ||
print(True and False) # && 

print("\n")
# functions/methods are represented as def  
# def requires a parameter after the name 
l = ["Money is a delusion", "Time is abstract", "Live like a passerby"]
# f"" allows you to concatinate variables in a string easier
print(f"before:{l}") 
def print_list(l):
    #for each string in the list, change each vowel to v
    for i, s in enumerate(l):
        word = ''
        for letter in s:
            
            vowels = ['a', 'e', 'i', 'o', 'u']
            if vowels.__contains__(letter):
                word += 'v'
            else:
                word += letter
            
        l[i] = word 

print_list(l)
print(l)


print('\n')

# return 
def give_me_my_money(amount):
    if amount < 1000:
        return'I hope it gets better for you'
    else:
        return 'I hope you continue to see goodness'

print(give_me_my_money(40))

#None is null
l
print(l) # prints nothing 
l = None
print(l)   # prints none 

print([1, 2] == [1, 2])
print([1, 2] == [1, 2, 2])
print([1, 2] == [1, 2, 3])
print([1, 2] is [1, 2, 3])
a = [1, 2, 3] 

b = a # b points to a's memory 
print(a is b)
print(b is a)
print(b == a)
print(b == [1,2,3])
print(b is [1,2,3]) # false. is 


#deepcopy()

from copy import deepcopy
c = deepcopy(a) # how to copy the contents of a list to another list 
print(c)

#can assign vatiable in parameter
def sum(a, b=1, c=2):
    return a + b + c
print(sum(1)) # dont need to pass in b or c 
print(sum(1, 2)) # here was pass in b as 2 instead of 1 

# getting the files
import os
print(os.listdir()) # list all files in directory 

# os.makedirs(directory, exist_ok=True) to make a new directory 
current_dir = os.getcwd() # get current working directory
file_name = "text_file.txt"
file_path = os.path.join(current_dir, file_name) # join the current directory with the file name
with open(file_path, 'w') as file: # Write to the file
    file.write("This is a sample text file.\n")
print(os.listdir()) 

with open(file_path, 'r') as file: # read the file
    print(file.readlines())

with open(file_path, 'w') as file: # Write to the file
    file.write("This is a sample text file.\n")
    file.write("This is the second line.")

with open(file_path, 'r') as file: # read the file
    for line in file:
        print(line.rstrip()) # remove the newline character 

# to append to a file (write rewrites the file)
with open(file_path, 'a') as file:
    file.write("This is the 3rd line.")

with open(file_path, 'r') as file: # read the file
    for line in file:
        print(line.rstrip())

# classes 
class Person:
    def __init__(self, name, age): # the constructor, where self must be in there
        self._age = age # self refers to the variables of the class 
        self._name = name
    def __str__(self): # similar to toString() in Java 
        return f"Name: {self._name}, Age: {self._age}"
    def older(self, age):
        return self._age > age

p = Person("John", 34)
print(p._name) # the _ is shows that it is private, but it's not enforced 
print(p.__str__())
print(p.older(30))

help(print) #print the documentation of the function 



    
