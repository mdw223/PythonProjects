animal = 'frog'
print(animal[3]) # strings can be indexed like lists, but strings are immutable
# slicing strings
print("I want an a" + animal[0:3])
print(animal[-1]) # gets the last letter 
print(animal[-3:]) # gets the last three letters
print(animal[:-3]) # gets all but the last three letters
print(animal[::2]) # gets every other letter

# can multiply strings
print(animal * 3)

#checking membership
print('f' in animal) # boolean 
print('x' not in animal)

# iterating
print('\nline 18')
for letter in animal:
    print(letter)
for i, letter in enumerate(animal): # for index, value in a list 
    print(i, letter)

# min() but cannot mix types
print(min(animal))
try:
    print(min("abc123"))
except:
    print("cannot mix types")

print(sum([1,2,3,4,5])) # sum() works on lists

print('hippo'.index('p')) # returns the index of the first occurence of the letter in the string
l = ['dog', 'cat', 'dog', 'bird']
print(l.index('dog')) # returns the index of the first occurence of the element in the list
a_1, a_2, a_3, a_4  = 'dog', 'cat', 'dog', 'bird' # unpacking allows for multiple assignments in one line
# the number of variables must match the number of elements in the list
print(a_1, a_2, a_3, a_4)

# creating a new list option 1
x = list() # or x = []
# creating a new list option 2
x = [1, 2, 3, 4, 5]
# creating a new list option 3
x = list(range(1, 6))
# creating a new list option 4
x = [i for i in range(1, 6)]
# creating a new list option 6
x = [i for i in range(1, 6) if i % 2 == 0]
# creating a new list option 7
x = [i**2 for i in range(1, 6)]
# creating a new list option 8
x = ['apple', 'banana', 'cherry', 3, 5]

tuple_1 = (1, 2, 3, 4, 5) # tuples are immutable
list_1 = list(tuple_1) # convert tuple to list
print(list_1)

del(x[0]) # deletes the first element in the list
del(x) # deletes the entire list
try:
    print(x)
except:
    print("x is not defined")

list_1.remove(4) # removes the first occurence of the element in the list
print(list_1)
del(list_1[len(list_1) - 1]) # deletes the first two elements in the list
print(list_1)
list_1.pop() # removes the last element in the list
print(list_1)
list_1.extend([4, 5, 6]) # adds the elements of the list to the end of the list
print(list_1)
list_1.insert(10,7) # inserts the element at the index
print(list_1)

# sets
del(list_1)

set_1 = {1, 2, 3, 4, 5} # sets are unordered and do not allow duplicates
set_1 = set([1, 2, 3, 4, 5]) # convert list to set

if (5 in set_1):
    set_1.remove(5)
print(set_1)
set_2 = set(range(3,6))
print(set_2)

# intersection
print("intersection:", str(set_1 & set_2))
# union
print("union:", str(set_1 | set_2))
# XOR
print("XOR:", str(set_1 ^ set_2)) # elements that are in set1 but not in set2 and vice versa
# difference
print("difference:", str(set_1 - set_2)) # elements that are in set1 but not in set2
# subset 
print("subset:", str(set_1 <= set_2)) # set1 is a subset of set2
# superset  
print("superset:", str(set_1 >= set_2)) # set1 contains set2

# dictionaries
x = dict() # or x = {}
x = {'a': 1, 'b': 2, 'c': 3}
x = dict(a=1, b=2, c=3)

del(x['a']) # deletes the key value pair
print(x)
print(x.get('b')) # returns the value of the key if it exists
x['d'] = 4 # adds a new key value pair
x['b'] = 5 # updates the value of the key
print(x)
# checking membership
print('b' in x)