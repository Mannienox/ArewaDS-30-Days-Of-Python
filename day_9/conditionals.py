# Exercises: Day 9

# Exercises: Level 1
# 1
age = int(input('Enter your age: '))
print('You are old enough to drive.') if age >= 18 else print(f'You need {18-age} years more to learn to drive')

# 2
age = int(input('Enter your age: '))
my_age = 25
if age < my_age:
    print(f'I am {my_age-age} years older than you') if my_age - age > 1 else print(f'I am 1 year older than you')
elif age > my_age:
    print(f'Your are {age - my_age} years older than me') if age - my_age > 1 else print(f'You are 1 year older than me')
else:
    print(f'Wow... I am also {age}.')

# 3
a = int(input('Enter num one: '))
b = int(input('Enter num two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

### Exercises: Level 2
score = int(input('Enter score: '))
if score >= 80 and score <= 100:
    print(f'Grade: A')
elif score >= 70 and score <= 79:
    print(f'Grade: B')
elif score >= 60 and score <= 69:
    print(f'Grade: C')
elif score >= 50 and score <= 59:
    print(f'Grade: D')
elif score >= 0 and score <= 49:
    print(f'Grade: F')
else:
    print('Out of range. Please enter a valid number between 0 and 100')


# 2
winter = ('december','january', 'february')
spring = ('march', 'april', 'may')
summer = ('june', 'july', 'august')
autumn = ('september', 'october', 'november')

# Collecting user response
month = input('Enter month: ')

# Applying conditionals
if month.lower() in winter:
    print('Season: Winter')
elif month.lower() in spring:
    print('Season: Spring')
elif month.lower() in summer:
    print('Season: Summer')
elif month.lower() in autumn:
    print('Season: Autumn')
else:
    print('Invalid month. Please check your spellings again')

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit = input('Enter fruit name: ')
if add_fruit.lower() not in fruits:
    fruits.append(add_fruit)
    print('New fruits list: ',fruits)
else:
    print('That fruit already exist in the list')

# 4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print('The middle skill is ', person['skills'][len(person['skills']) // 2])

if 'skills' in person.keys():
    print('python' in person['skills'])

if set(person['skills']) == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(set(person['skills'])):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(set(person['skills'])):
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")