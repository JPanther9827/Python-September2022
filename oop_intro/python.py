# OOP (object orientated programming)
# objects - things, items, they can do things, they have properties / attributes that describe
# emphasizes grouping data and funtionality together in entities known as objects
# method is just a function belonging to a class
# self is a reference to the actual instant
# the definition (def) is a blueprint for a custom data type that we define and when we use that blueprint to create an object
# that process is called initation
#  class is the  blueprint, object is the thing created from the blueprint
# (self, name, color, age, breed) is your parameter
# self.color = color,self.age = age, self.breed = breed. <-- These are your attributes
# indentation is important!
cat1 = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}

cat2 = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}
# the __init__ has two underscores, not one
# use your parameters to build out the hard code
# class Cat():
#     def __init__(self):
#         self.name = "Felix"
#         self.color = "Black"
#         self.age = 50
#         self.breed = "cartoon"

class Cat():
    def __init__(self, name, color, age, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

    def print_info(self):
        print(f"Name: {self.name} color: {self.color} age: {self.age} breed: {self.breed} ")
        #  your injecting a variable inside the {}
        # self references the current instant that that method got called on


    def meow(self):
        print(f"{self.name} lets out a cry: MEOOWWW")



cat1 = Cat("Scar", "dark brown", 3, 'lion')


print(cat1.name)
print(cat1.color)

cat1.print_info()
cat1.meow()
#  your provoking a method by using a () to make that function work
# your referencing that variable to get the output your looking for in the print function