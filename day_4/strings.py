#Exercise: Day 4
#1
list_of_strings = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(list_of_strings))

#2
list_of_strings = ['Coding', 'For' , 'All' ]
print(' '.join(list_of_strings))

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[1:])

#10
print(company.index('Coding'))

#11
print(company.replace('Coding','Python'))

#12
new_company = company.replace('Coding', 'Python')
new_company = new_company.replace('All', 'Everyone')
print(new_company)

#13
print(company.split())

#14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = companies.split(',')
print(companies)

#15
print(company[0])       #C

#16
print(company.rindex('l'))      #13

#17
print(company[10])      # (empty space)

#18
acronym = []
for x in company.split():
    acronym.append(x[0])
print(''.join(acronym))             #CFA

#19
acronym = []
for x in new_company.split():
    acronym.append(x[0])
print(''.join(acronym))             #PFE

#20
print(company.index('C'))           #0

#21
print(company.index('F'))           #7

#22
print(company.rfind('l'))       #13

#23
message = 'You cannot end a sentence with because because because is a conjunction'
print(message.index('because'))             #31

#24
print(message.rindex('because'))            #47

#25
print(message.replace('because ',''))       #You cannot end a sentence with is a conjunction

#26
print(message.find('because'))              #31

#27
print(message.replace('because ',''))       #You cannot end a sentence with is a conjunction

#28
sub_string = 'Coding'
print(company.startswith(sub_string))       #True

#29
sub_string = 'coding'
print(company.endswith(sub_string))     #False

#30
print('  Coding for All  '.strip())         #Coding for All

#31
print('30DaysOfPython'.isidentifier())          #False
print('thirty_days_of_python'.isidentifier())   #True

#32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

#33
print('I am enjoying this challenge.\nI just wonder what is next.')

#34
print('Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki')

#35
print(f'radius = 10\n'
      f'area = 3.14 * radius ** 2\n'
      f'The area of a circle with radius 10 is {3.14 * 10 ** 2}')

#36
print('{} + {} = {}'.format(8,6,8+6))
print('{} - {} = {}'.format(8,6,8-6))
print('{} * {} = {}'.format(8,6,8*6))
print('{} / {} = {:.2f}'.format(8,6,8/6))
print('{} % {} = {}'.format(8,6,8%6))
print('{} // {} = {}'.format(8,6,8//6))
print('{} ** {} = {}'.format(8,6,8**6))
