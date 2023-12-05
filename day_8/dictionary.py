# Exercises; Day 8

# 1
dog = {}

#2
dog['Name'] = 'Alice'
dog['Colour'] = 'White'
dog['Breed'] = 'German'
dog['Legs'] = 50
dog['Age'] = 2
print(dog)

#3
student = {
    'first_name' : 'Tibeg Damaris',
    'last_name' : 'Amos',
    'gender' : 'Female',
    'age' : 21,
    'marital_status' : 'Single',
    'skills' : ['Sewing', 'gossipping'],
    'country' : 'Nigeria',
    'city' : 'Kaduna',
    'address' : 'Ungwan Bulus, Sabon Tasha, Kaduna'
}
print((student))

#4
print(len(student))

#5
print(type(student['skills']))

#6
student['skills'].append('Solving maths')
print(student['skills'])

#7
keys = list(student.keys())
print(keys)

#8
values = list(student.values())
print(values)

#9
student_list = list(student.items())
print(student_list)

#10
del student['address']
print(student)

#11
del dog