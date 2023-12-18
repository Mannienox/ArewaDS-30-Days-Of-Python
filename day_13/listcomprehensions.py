# Exercises: Day 12
# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [x for x in numbers if x <= 0]
print(filtered_list)

# 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [x for element in list_of_lists for row in element for x in row]
print(flattened_list)

# 3
print([(x, x**0, x**1, x**2, x**3, x**4, x**5) for x in range(11)])

# 4
countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]
flattened_list = [list(x) for row in countries for x in row]
print(flattened_list)

# 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_of_countries = [{x:y} for row in countries for x,y in row]
print(dict_of_countries)


# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(x) for row in names for x in row]
print(concatenated_names)

# 7
slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
print(slope(1,2,3,4))