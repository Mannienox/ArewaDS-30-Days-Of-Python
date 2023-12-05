# Day 2: 30 Days of python programming
#Exercise: Level 1
first_name = "Manasseh"
last_name = "Ibrahim"
full_name = "Ibrahim Manasseh"
country = "Nigeria"
city = "Kaduna"
age = 25
year = 2023
is_married = False
is_true = True
is_light_on = True
a,b,c = 2,3,4

#Exercise: Level 2
# 1: Checking types of variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

# 2: finding the length of first name
print(len(first_name))

# 3: Comparing the lengths of first name and last name
print(len(first_name)<len(last_name))

# 4: Calculator
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_two**num_one
floor_division = num_one//num_two

# 5: circle calculator
import math
radius = 30
area_of_circle = math.pi*radius**2
circum_of_circle = 2*math.pi*radius
radius = float(input('Enter radius: '))
area_of_circle = math.pi*radius**2

# 6: Getting inputs from user
first_name = input("First Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input("Age: ")

# 7: python keywords
import keyword
print(keyword.kwlist)