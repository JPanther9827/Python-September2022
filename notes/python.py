# RANGE
#build in function
#range(START, END_NOT_INCLUDED, STEP )
#range(start, stop, step)
# start defaults at zero and exits at number provided
# stop begins at start number and exits at index of stop number provided
# step increases by provided integer until reaching index of stop integer

for x in range(1, 8):
    print(x)

print("================================")

code_languages = ["js", "python", "c++", "java", "ruby", "c#"]
print(code_languages[1])

print("================================")

for i in range(len(code_languages)):
    if code_languages[i] == "python":
        code_languages[i] = "This is what I am learning right now."

print("================================")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in nums:
    print(sum)
    sum += num

print(sum)

print("================================")

# function add(){

# }


def add(num1, num2):
    # print("we are adding here!", num1, num2)
    # print(num1+num2)
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    print("we are subtracting here!")
    return num1 - num2


def multiply(num1, num2, word):
    print("we are multiplying here!", num1, num2, word)
    print(type(num1))
    print(type(num2))
    print(type(word))
    return num1 * num2


x = add(5, 9)
print(subtract(1, -1))
print(multiply(2, 2, "3"))

# (=======================================================================================================)

# LIST - Literally Indexed, Single Things (Stores one item at an index)
# DICT - Don't Index, Coupled Things (Stores key value pairs) "Curlies hold the keys"

# Definition:

list = ['red','blue','green'] # indices 0, 1, 2

dict = {
    'color1': 'red',
    'color2': 'blue',
    'color3': 'green'
}

#Access:
#notice both use brackets but dict uses keys, list uses indices
list[2] #green
dict['color3'] #green

#Assignment

list[2] = 'pink' #updates third index to 'pink'
dict['color3'] = 'pink' #updates value stored paired with key 'color3' to 'pink'

#Adding to list/dict
list.append("orange")
dict['color4'] = 'orange'

#Removing from list/dict
list.pop(2) #pop an index
del list[2] #removes index 2 without returning it

color2 = dict.pop('color2') #pop a KVP by key and return it

del dict['color4'] #deletes on KVP without returning it
dict.clear() #clears whole dict

# (==============================================================================================================)
"""
OOP -- THE FOUR PILLARS
Encapsulation --
    Grouping code together into these entities we call classes
Inheritance
    Ability to create subclasses that have all the attributes and methods of the parent class
    key word super() will access the parent class
Polymorphism
    Child classes can have different definitions for the same methods, different values for the same attributes by 
    overwriting the values from the parent
Abstraction
    Abstraction is an extension of Encapsulation, and we can hide attributes or methods that a Barista doesn't need to know about, like a CoffeeM. That way the Barista can make a cup of coffee in a simpler manner
"""

"""
Packages + Modules
Modules are just .py files that hold functionality -- they might be made up of functions, classes, variables, etc
Packages -- are directories that hold multiple modules
from game_classes import character
from game_classes.character import Character
"""

""" 
input()
a function to get info from the user
"""