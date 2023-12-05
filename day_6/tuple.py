# Exercises: Level !
#1
my_tuple = ()

#2
brothers = ('Blessing',  'Patience')
sisters = ('Amen', 'Fumen', 'Stephen', "Zackariah")

#3
siblings = brothers + sisters
print(siblings)

#4
print(len(siblings))

#5
parents = ('Ibrahim', 'Paulina')
family_members = parents+siblings
print(family_members)


# Exercises: Level 2

#1
parents = family_members[:2]
siblings = family_members[2:]

#2
fruits = ('Mango', 'Apple', 'Pea')
vegetables = ('Ogu leaves', 'Water leaves', 'Cabage')
animal_products = ('Skin', 'Meat', 'Milk')
food_stuff_tp = fruits + vegetables + animal_products

#3
food_stuff_it = list(food_stuff_tp)

#4
if len(food_stuff_tp)%2 == 1:
    middle_item = food_stuff_tp[len(food_stuff_tp)//2]
    print(middle_item)
else:
    middle_items = tuple(food_stuff_tp[len(food_stuff_tp) // 2 - 1], food_stuff_tp[len(food_stuff_tp)//2])
    print(middle_items)

#5
part = food_stuff_tp[:3]
print(part)
part = food_stuff_tp[-3:]
print(part)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)