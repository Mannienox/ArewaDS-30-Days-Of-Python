# Exercises: Day 12
# Exercises : Level 1

# 1
from random import *
def random_user_id ():
    possible_outcomes = 'abcdefghijklmnopqrstuvwxyz0123456789'
    rand_6digit = choices(possible_outcomes, k=6)  # Collects 6 digits in a list from message.
    user_id = ''.join(rand_6digit)
    return user_id


print(random_user_id())


# 2
def user_id_gen_by_user():
    possible_outcomes = 'abcdefghijklmnopqrstuvwxyz0123456789'
    num_of_characters = input('Number of Characters: ')
    num_of_ids = input('Number of IDs: ')
    for x in range(int(num_of_ids)):
        rand_id = ''.join(choices(possible_outcomes, k = int(num_of_characters)))
        print(rand_id)
user_id_gen_by_user()

# 3
def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb = f'rgb({r}, {g}, {b})'
    return rgb
print(rgb_color_gen())

# Exercises: Level 2
# 1
from secrets import token_hex
def list_of_hexa_colors():
    hex_colours = []

    number_of_hexColor = input('No of hexadecimal colours: ')
    for i in range(int(number_of_hexColor)):
        hex_no = token_hex(3)  # This will print a random 6 digit hexa decimal number
        hex_color = '#'+hex_no
        hex_colours.append(hex_color)
    return hex_colours

print(list_of_hexa_colors())

# 2
def rgb_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    number_of_rgb = int(input('Enter number of rgb: '))
    rgbs = []
    for i in range(number_of_rgb):
        rgb = f'rgb({r}, {g}, {b})'
        rgbs.append(rgb)
    return rgbs
print(rgb_color())


# 3
def generate_colors(colour_type, number):
    colours = []
    if colour_type == 'hexa':
        for i in range(int(number)):
            hex_no = token_hex(3)  # This will print a random 6 digit hexa decimal number
            hex_color = '#' + hex_no
            colours.append(hex_color)
    elif colour_type == 'rgb':
        for i in range(int(number)):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            rgb = f'rgb({r}, {g}, {b})'
            colours.append(rgb)

    else:
        colours = "Invalid Colour type. Please use 'hexa' or 'rgb'"
    print(colours)
generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)

# Exercises: Level 3
# 1
def shuffle_list(original_list):
    shuffled_list = sample(original_list, k = 3) # The sample function works like the choices except that when it works, no repitions are noticed
    return shuffled_list
print(shuffle_list([1,2,3]))


#2
def array_of_seven ():
    array = '0123456789'
    random_7digits = ''.join(sample(array, k=7))
    return random_7digits
print(array_of_seven())