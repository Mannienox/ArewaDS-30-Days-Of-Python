# Exercises: Day 18
# Exercises: Level 1

# 1
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
word_count = []
modified_paragraph = paragraph.replace('.', '') # to take away the .
print(modified_paragraph)
list_words = re.split(' ', modified_paragraph)  # to split
for word in set(list_words):
    count = list_words.count(word)
    word_count.append((count, word))
sorted_word_count = sorted(word_count, reverse=True)
print(sorted_word_count)

# 2
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
points = re.findall(r'[-]*\d+', text, re.I)
sorted_points = [int(x) for x in points]
print('points = ',points)
print('sorted_points = ', sorted_points)
print('distance = ', sorted_points[-1],'- (',sorted_points[0],') =', sorted_points[-1] - sorted_points[0])

# Exercises: Level 2
# 1
from keyword import iskeyword
def is_valid_variable(string):
    state = False
    if string.isidentifier():
        if iskeyword(string):
            state = False
        else:
            state = True
    print(state)
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True



# Exercises: Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text (sentence):
    cleaned_sentence = re.sub(r'[%@#$&;!,.?]', '', sentence)
    print(cleaned_sentence)
    word_count = []
    list_words = re.split(' ', cleaned_sentence)  # to split
    for word in set(list_words):
        count = list_words.count(word)
        word_count.append((count, word))
    sorted_word_count = sorted(word_count, reverse=True)
    return sorted_word_count[:3]

print(clean_text(sentence))
