l = [i for i in range(10)] # quickly creates a list 

print(l)

l = [i if i % 2 == 0 else 0 for i in range(10)] # if statement in list construction
print(l)

l = [0]*5 # creates a list of 5 zeros 
print(l)

#concatinate arrays
l = [1, 2, 3] + [4, 5]
print(l)

#zip function does element wise operations
l = [i for i in zip(range(3), range(3, 6))]
print(l) # a list of tuples 

l = [(a, b) for a, b in zip(range(3), range(3, 6))]
print(l)

l = {a:b for a, b in zip(range(3), range(3, 6))} # dictionary 
print(l)

# convert a number ASCII to a char
print(chr(65))
print(ord('A'))

l = {k:chr(k) for k in range(65,65+26)} # dictionary 
print(l)

# copy import library
from copy import deepcopy

d = deepcopy(l)
print("\n" + str(d))

import copy as cp # can use cp 
l = [1, 2, 3]
# d = cp.copy(l) is if l is a string
d = cp.deepcopy(l)
print("\n" + str(d))

# getting the files
import os
print(os.listdir()) # list all files in directory 
# os.makedirs(directory, exist_ok=True) to make a new directory 
current_dir = os.getcwd() # get current working directory
file_name = "text.py"
file_path = os.path.join(current_dir, file_name) # join the current directory with the file name
with open(file_path, 'w') as file: # Write to the file
    file.write("x = 10")
    file.write("\n")
    file.write("if x >= 13:")
    file.write('    print("you are a teen")')
    file.write("\n" + "else:" + "\n") # use tab to paste suggestion
    file.write('    print("you are not a teen")')
print("\n")
with open(file_path, 'r') as file: # Read the file
    for line in file:
        print(line.strip())

print("\n")
# will execute the code
import subprocess # importing the text file in directory to run it
subprocess.run(["python", file_path]) # run the file

with open(file_path, 'a') as file: # Write to the file")
    file.write("\n")
    file.write("def mult(a, b):" + "\n")
    file.write('    return a*b')

# file.close() # close the file 
# don't need to close the file when using 'with' open
''' # Open a file
file = open("example.txt", "w")

# Write to the file
file.write("Hello, world!")

# Close the file
file.close()
'''
print(file.closed)  # False (file is open)

import text as t
print(t.mult(2, 3)) # calls the function in text file 