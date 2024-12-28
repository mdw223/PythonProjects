from operator import contains


l = [1, 2, 3] 
l.append(4)
l.insert(0, 0)
print(l.count(1)) # counts how many times 1 is in the list
l.reverse()
print(l)

#make l an empty list
l = []
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            l.append(i + j)
print(l)

# dictionary with a key and value, similar to hash map in Java
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a']) # returns its value 

#change a value in the dictionary
d['a'] = 4
print(d)
print(d.keys()) # makes a list of keys of the dictionary
for letter in d.keys():
    d[letter] += 10

print(d)


# splitting a stirng into a list
s = "What's up everyone my name is Malik"
print(s)
s_1 = s.split()  # the default is ' 
print(s_1)
s_2 = s.split(' ') 
print(s_2)
vowels = 'aeiou'
def split_at_vowels(s, vowels):
    l = ''
    for letter in s:
        if letter in vowels:
            l += " " + letter
        else:
            l += letter
    return l
print(split_at_vowels(s, vowels))

# convert strings to upper
print(s.upper())


''' Python Tuple is a collection of objects separated by commas. 
A tuple is similar to a Python list in terms of indexing, nested objects, 
and repetition but the main difference between both is Python tuple is immutable, 
unlike the Python list which is mutable.'''
t = (1, 2, 3, 4)
print(t)
print(t[0])

# ordering a list
l = ["Malik", 'Aisha', 'Zainab', 'Bilal']
print(sorted(l))
# sorted(l) returns a new list that is sorted l 
# l.sort() sorts the list and changes its original content
l.sort()
print(l)

# set(), an underordered collection of unique elements 
s = set("My name is Malik")
print(s)

t = (1, 2)

print(t[0])
try: # try and except to catch errors 
    t[0] = 1
except:
    print("error")

try:
    print("Before")
    print(print3)
    print("After")
except NameError:
    print("Produced an exception")

# user input 
user = input("How much money do you have?: ")
quit = False
while (not quit): 
    # check if user is a number
    try: 
        num = int(user) / 2
        print("Thank you, here's half:", str(num))
        quit = True
    except:
        user = input("Give me an amount pls!: ")
    