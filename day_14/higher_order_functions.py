# Exercises: Day 14
# Exercises: Level 1

# 1
'''
DIFFERENCE BETWEEN MAP, FILTER AND REDUCE
Although all of them take in two arguments, a function and an iterable, the map function performs the function for all iterables.
The filter function on the other hand returns an array of the iterables that satisfy the filtered criteria.
While the reduce function only returns a single value depending on what the parametric function is programmed to.

'''

# 2
'''
DIFFERENCES BETWEEN HIGHER ORDER FUNCTIONS, CLOSURE AND DECORATOR
When we have another function taking another function as a parameter and returning the function as a return value, then we call the function a higher order function.
Closure is the ability of a nested function to access the outer scope of the enclosing function
While  decorator actually adds functionality to a python function without modifying the function's structure
'''

# 3
import math
numbers = list(range(0,181,30))
def cosine(x):
    a = math.cos(3.142*x/180)
    if a != 1:
        a = f'{a:.4}'

    return tuple([x,a])


perfect_squares_list = map(cosine, numbers)
print(list(perfect_squares_list))


# 4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print('\n')
for counrty in countries:
    print(counrty)

# 5
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print('\n')
for name in names:
    print(name)

# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n')
for number in numbers:
    print(number)

# Exercises: Level 2
# 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
new_list = map(lambda country: country.upper(), countries)
new_list = list(new_list)
print('\n')
print(new_list)

# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x**2, numbers))
print('\n')
print(new_list)

# 3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
new_list = map(lambda name: name.upper(), names)
new_list = list(new_list)
print('\n')
print(new_list)

# 4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def land_in_country(country):
    if 'land' in country:
        return True
    return False


new_list = filter(land_in_country, countries)
new_list = list(new_list)
print('Countries with "land" are: ', new_list)


# 5
def six_characters (country):
    if len(country) == 6:
        return True
    return False

new_list = filter(six_characters, countries)
new_list = list(new_list)
print('Countries having exactly 6 characters: ', new_list)


# 6
def six_characters_or_more (country):
    if len(country) >= 6:
        return True
    return False

new_list = filter(six_characters_or_more, countries)
new_list = list(new_list)
print('Countries with 6 characters and more: ', new_list)


# 7
def six_characters_or_more (country):
    if country.startswith('E'):
        return True
    return False

new_list = filter(six_characters_or_more, countries)
new_list = list(new_list)
print('Countries that start with letter "E": ', new_list)


# 8
from pyterator import iterate
def squares(x):
    sqr = x**2
    return sqr
def check_odd(x):
    if x%2 != 0:
        return True
    return False
chained = iterate(numbers).map(squares).filter(check_odd)
print(list(chained))


# 9
def get_string_lists (*lst):
    string_lst = []
    for x in lst:
        if type(x) == type('mannie'):
            return True
        return False

lst = [1, '2', 3, '4', 5, '6', 7, '8', 9, '10']
new_list = filter(get_string_lists, lst)
print(list(new_list))
