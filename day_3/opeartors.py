#1
age = 25
#2
height = 5.9
#3
z = 2-2j
#4
b = float(input("Enter base: "))
h = float(input("Enter height: "))
area_of_triangle = 0.5*b*h
print('The area of the triangle is ', area_of_triangle)

#5
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_of_triangle = a+b+c
print('The perimeter of the triangle is ', perimeter_of_triangle)

#6
length = float(input("Length: "))
breadth = float(input("breadth: "))
area = length*breadth
perimeter = 2*length*breadth
print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

#7
r = float(input('Enter radius of circle: '))
area = 3.14*r**2
perimeter = 2*3.14*r

#8
#when x = 0, y = -2 and when y = 0, x = 1. This implies that the straight line passes through (0,-2) and (1,0)
slope = (0-(-2))/(1-0)
# Alternatively, the slope is the coefficient of x in the equation which is simply 2, that is by comparing the equation to the standard equation of a straight line, y = mx + c

# The x-intercept occurs where y = 0. So we make x the subject of the formula and set y=0
y=0
x = (y+2)/2
x_intercept = x
# The y intercept occurs where x = 0. so we set x = 0
x = 0
y = 2*x -2
y_intercept = y

print('Slope = ', slope)
print('x_intercept = ', x_intercept)
print('y_intercept', y_intercept)


#9
x1,y1 = 2,2
x2,y2 = 6,10
m = (y2-y1)/(x2-x1)
dist = ((x2-x1)**2 - (y2-y1)**2)**(1/2)
print('Slope is ', m)
print('Euclidian distance is ', dist)

#10
print(slope < m)

#11
values_of_x = range(-10,10)
for x in values_of_x:
    y = x**2 + 6*x + 9
    if y == 0:
        print('When x = ',x,' y = 0')

#12
print(len('python'))
print(len('dragon'))
print(len('python')<len('dragon'))

#13
print('on' in ('python' and 'dragon'))

#14
print('jagon' in 'I hope this course is not full of jagon')

#15
print('on' not in ('python' and 'dragon'))

#16
length = len('python')
length = float(length)
length = str(length)

#17. I'll check if x%2 returns 0 or 1, since any number divided by 2 returns either a reminder of 2 or 1. if x%1 returns 0, then the number is even

#18
print(7//3 == int(2.7))

#19
print(type('10') == type(10))

#20
print(int(float('9.8')) == 10)  #int('9.8') returns an error

#21: earnings Calculator
hours = input('Enter hours: ')
rate = input('Enter Rate per hour: ')
earning = float(hours)*float(rate)
print('Your weekly earning is ', earning)

#22
years = input("Enter number of years you have lived: ")
number_of_seconds = 60*60*24*365*int(years)
print('You have lived for ', number_of_seconds, ' seconds')

#23
for x in range(1,6 ):
    print(x,'\t1\t',x,'\t',x**2,'\t',x**3)