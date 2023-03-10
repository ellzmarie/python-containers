
# <!-- Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name. -->

students = ["Brooklyn", "Reign", "Valor"]

print(students[1])
print(students[-1])

print('-----------------------------------------')
# <!-- Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a forloop to print out the string "food goes here is a good food". -->

foods = ('apple', 'banana', 'cherries', 'mangos')

for i in range(len(foods)):
    print(foods[i] + " is a good food.")

print('-----------------------------------------')

# <!-- Exercise 3
# Using a forloop, print just the last two food strings from foods. -->

for food in foods[-2:]:
    print(food)

print('-----------------------------------------')

# <!-- Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population" -->

home_town = {
    "city": "sacramento",
    "state": "california",
    "population": "2555632"
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

print('-----------------------------------------')
# <!-- Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000" -->

for key, val in home_town.items():
	print(f"{key} = {val}")

print('-----------------------------------------')

# <!-- Exercise 6
# Create an empty list named cohort.
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }
# Iterate over cohortprinting out each element. -->

cohort = []
student_names = ['Tina', 'Brooklyn', 'Reign', 'Valor']

for student in student_names:
  cohort.append({
    'student': student,
    'fav_food': 'Cheeseburger'
  })

for student in cohort:
  print(student)


print('-----------------------------------------')
# <!-- Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string. -->

awesome_students = []

for student in student_names:
	print(f'{student} is awesome!')


print('-----------------------------------------')
# <!-- Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a. -->

foods = ('apple', 'banana', 'cherries', 'mangos')

for food in foods: 
     if 'a' in food:
          print(food)