# Variables ---- a container where you can keep data

name = "Javaris"
number_of_dogs = 1
# variables are names using snake case -- all lower case separarted by underscores
# expection: classes will be capitalized
# let var const <-- no need to these in python 

# Datatypes
# primitve

# numbers

num = []
float_num = 8.5



# strings
string = "collection of characters"
string2 = "String 2"
f_string = f'{name} has {number_of_dogs} dogs'
# type casting functions
num5 = int("5")

string5 = str(5)


print(f_string)

# booleans
bool1 = True
bool2 = False

# composite
# lists
list = [1,2,3,4,5]
# zero indexed
list[2] = 100
print(list)
# list functions
len(list) 
# returns length of the list
min(list)
# return lowest value from the list
max(list)
# highest value

# list methods
# list.reverse()
# list.sort(reverse = True)

list.append(245877)
# append to add a value to a list
list.remove(100)
# removes a VALUE
list.pop(0)
# notionally take on an INDEX to pop
print(list)
# tuple IMMUTABLE list of values accessed by index
my_tuple = (1,2,3,4,5)
print(my_tuple[3])
# my_tuple[3] = 12 type error

# dictionaries
# KEY VALUE PAIRS:
dog = {
    'name': 'Mama',
    'age': 50,
    'breed': 'Beagle'
}
# access
print(dog['name'])
# assignment
# dog['color'] = "Dark-brown"
print(dog)

# check if key exists
if 'color' in dog:
    print(dog['color'])
else:
    print("key not found")

# removing from dict
# del dog['breed']
# breed = dog.pop("breed")
# dog.clear()
# print(breed)
# print(dog)



# string = "Don't tell me what to do"

# Conditionals -- an expression returns a boolean value that we will use to determine topic
# user pass for empty code blocks
x = 6
if x == 5:
    print("x is 5")
elif x > 5:
    print("greater than 5")
else:
    print("x is not 5 and not greater than 5")