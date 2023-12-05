#Exercises: Day 7
# Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1
print(len(it_companies))

# 2
it_companies.add('Twitter')

# 3
it_companies.update(['Whatsapp', 'Instagram', 'Yahoo'])

# 4
it_companies.pop()

# 5. While both pop out specific elements from a set, tHe difference between the remove and discard methods is that the
# remove method returns an error if the element does not exist but the discard method doesn't.


# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1
print(A.union(B))

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))
del A, B


# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(age)

# 1
print(len(age))
print(len(ages_set))
print(len(age) < len(ages_set))

# 2
# A list is an ordered collection of mutable objects enclosed in a pair of square brackets and it can contain mutiple data types
# A tuple on the other hand is an immutable list. Objects in a tuple are enclosed in a pair of parenthesis
# A set is an unordered collectoin of mutable objects enclosed within a pair of curly braces

sentence = 'I am a teacher and I love to inspire and teach people'
st = set(sentence.split())
print(st)