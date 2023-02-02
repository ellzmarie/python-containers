# Python containers:
    # Dictionaries - object
    # Lists - Array
    # Tuples - n/a

#####################
# Dictionaries #
#######################
    # A dictionary provides a container for key: valuepairs. We can refer to key: valuepairs as items.

    # Dictionaries have a class (type) of dict.

student = {
    "name": "Fred",
    "course": "SEIR",
    "current_week": {
        "22": True
    }
}

# the syntax is exactly like JS but you must wrap the keys in quotes
# Dictionaries are mutable (changable > update, add) - can be altered, changed, added to, removed from 
# when looping through an object, the order is random

# There is no dot notation in Python
name = student['name'] # use bracket notation to access a key
print(name)
###########################
###### .get() method ######
# birthdate = student["birthdate"]
# print(birthdate)
print(student.get("birthdate")) # returns NONE
print(student.get("name")) # returns value just like bracket notation > FRED
print(student.get("current_week").get("22")) # you can chain .get() for accessing deeper nested dictionaries
print(student.get("birthdate", "04-04-1985")) # this does not alter the original dictionary > wasn't added into the "student" dictionary
print(student)

###########################
###### In Operator ######
    # checks to see if a value is "IN" the iterable

if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")

###########################
###### Adding Items ######
student["age"] = 21 # use bracket notation

############################
###### Deleting Items ######
# used to delete an item from the dictionary
del student['age']
# verify that item was deleted
'age' in student
print('age' in student)

#############################
###### Number of Items ######
# use the built-in len function to retrieve the number of items in a dictionary
print(len(student))

##########################################
###### Looping through dictionaries ######
for key, val in student.items(): # .items() is required to get the key and val for each iteration
    print(f"{key} = {student[key]}")
    print(f'{key} = {val}')
    
# the student.items() call above returns a wrapped set of tuples:
student.items()
    # > dict_items([('name', 'Tina'), ('course', 'SEI')])

where_my_things_are = {
    "car_key": "hanging on door",
    "shoes": "in the closet",
    "chalk": "in a basket",
    "bubbles_machine": "in the backyard"
}
for thing, location in where_my_things_are.items(): 
        print(f"My {thing} is kept {location}")

############################
# LISTS #
###########################

# type is a list
# can contain 0 or more items of any data type

###### Basic Syntax
colors = ["red", "blue", "green"]

# to get the length of the list, use:
print(len(colors))

# lists are a sequence type
# lists are mutable
idx = 2
colors[idx] # pass in an index number to get the value at that index

# negative numbers can be used to access items to the back of the list 
[0, 1, 2, 3, 4, 5, 6]
[-7, -6, -5, -4, -3, -2, -1]

####### Assigning Items - by index
colors[2] = 'purple'
colors[-1] = 'brown'
print(colors)

###### Adding items > .append()
# add something to the back of the list (does not return), we use: 
colors.append("green")
print(colors)

###### Adding multiple items (appends to the end) > .extend()
colors.extend(["orange", "black"])
print(colors)

###### Insert items at a specific point > .insert()
colors.insert(1, "yellow")
print(colors)

###### Deleting items 
    # .pop() add an index number to be more specific
    # del
    # .remove()
    # .clear()
colors.pop(2) # will remove and return the item at index 2
print(colors)

del colors[3] # will delete the value at index 3

colors.remove("orange") # will remove the first match

# clear the entire list
    # >>>> colors.clear() # removes all items from the list

my_colors = colors # changing original will change the copy
print(my_colors)
colors.append("teal")
print(my_colors)

###########################
###### Looping ######
colors = ["red", "green", "blue"]

for color in colors: # you can loop over each and access the value only
     print(color)

for idx, color in enumerate(colors): # you can loop through and access both value and index
     print(idx, color)

############################
# LIST COMPREHENSION#
###########################
# <expression> for <item> in <list>
nums = [1,2,3,4,5,6,7,8,9,10]

squares = []
for num in nums:
     squares.append(num * num)
print(squares)

######## OR ############
# a list comprehension will condense the code to this:
# I want num x num for each num in nums
squares = [num * num for num in nums]

######## MORE COMPLEX ########
nums = [1,2,3,4,5,6,7,8,9,10]

even_squares = []
for num in nums: 
     square = num * num
     if square % 2 == 0:
          even_squares.append(square)
print(even_squares)

# list comprehension for the above code
# I want num * num for each num in nums if num * num is even
even_squares = [num * num for num in nums if (num * num) % 2 == 0]
print(even_squares)

# List comprehensions create a new list from a logical statement

############################
# TUPLES #
###########################
# Tuples are just like lists
# type of tuple
# syntax uses parentheses () instead of []
# tuples are immutable - no changing them


color_wheel = ('red', 'green', 'blue') # this is a tuple
color_wheel = 'red', 'green', 'blue' # this is also a tuple

hello_tuple = ('hello',) # you need a comma if your tuple has just one item
hello_tuple = 'hello',

# python can iterate through a tuple faster than a list

# getting things out of a tuple
colors = ('red', 'green', 'blue')

green = colors[1] # reference indexes just like you do in a list
print(colors[1])

blue_idx = colors.index('blue') # will return the index of the first match for blue
print(blue_idx)

for idx, color in enumerate(colors): # use the enumerate with tuples
     print(idx, color)

# unpacking a Tuple
# pulling values out of a tuple setting them equal to a var to be manipulated

color_wheel = ('red', 'green', 'blue')
red, green, blue = colors

###########################
###### Slicing Sequences ######
# Sequence - lists, tuples, string - ordered, have indexes
# Slice [m:n] # slices up to but not including the number on the right
name = "Alexandria"[0:4]
print(name)

color_wheel = ('red', 'green', 'blue')[:2] # the slice makes a copy starting at the beginning
print(color_wheel)

nums = [1,2,3,4,5,6,7,8,9,10][1:] # omitting the sequence up to the number given all the way 
print(nums)

fruit = ('apples', 'bananas', 'oranges')
fruit_copy = fruit[:]
print(fruit_copy)