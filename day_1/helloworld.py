# Exercise: Level 2
# 1: Check python version
import sys
print('Python version: ', sys.version)

# 2: operations between 3 and 4
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

# 3: Working with strings
print('Manasseh')
print('Ibrahim')
print('Nigeria')
print('I am surely enjoying python')

# 4: Checking data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Manasseh'))
print(type('Ibrahim'))
print(type('Nigeria'))

# Exercise: Level 3
# 1: Examples
print('1 is an example of an integer')            # Example of integers
print('1.5 is an example of a float ')     # Example of floats
print('1-2j is an example of a complex number')     # Example of complex numbers
print("'Mannie' is an example of a string")   # Example of strings
print('True is an example of a boolean')    # Example of boolean
print('[1, "Amina", False] is an example of a list')    # Example of lists
print('(1,2) is an example of a tuple')         #Example of tuples
print('{1,3,5,7,9} is an example of a set') # Example of sets
print("{'Name':'Ibrahim Manasseh', 'Age':25} is an example of a dictionary")       # Example of a Dictionary

# 2: Finding Euclidian distance between (2,3) and (10,8)
distance = ((10-2)**2 + (8-3)**2)**(1/2)    # We could also use distance = math.dist((2,3), (10,8)) after importing the math function
print('The Euclidian distance between (2,3) and (10,8) is ', distance)