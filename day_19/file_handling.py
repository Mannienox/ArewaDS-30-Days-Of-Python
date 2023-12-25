# Exercises: Day 19
# Exercises: Level 1
import csv
import operator
# 1
import re
def counter (file_name):
    try:
        with open(file_name) as file:
            txt = file.read()
            list_of_lines = txt.splitlines()
            number_of_lines = len(list_of_lines)

            # for count lines
            #file = file.read()
            cleaned_file_name = re.sub(r'[^a-zA-Z0-9\n ]', '', txt)
            words_list = re.split(' |\n', cleaned_file_name)
            words_count = len(words_list)
            return f'In {file_name}, we have {number_of_lines} lines and {words_count} words'
    except:
        return 'File does not exist!'
# a)
print(counter('../data/obama_speech.txt'))

# b)
print(counter('../data/michelle_obama_speech.txt'))

# c)
print(counter('../data/donald_speech.txt'))

# d)
print(counter('../data/melina_trump_speech.txt'))


# 2
import json
def most_spoken_languages(filename, top):
    with open(filename, encoding='utf-8') as file:
        countries_string = file.read()
        countries_data = json.loads(countries_string) # changes this to a list of dictionaries

        # collecting languages in one list
        languages_list = []
        for country in countries_data:
            languages_list = languages_list + country['languages']

        # collecting each language and its count in a list of tuple
        languages_frequency = []
        for language in set(languages_list):
            count_of_language = languages_list.count(language)
            languages_frequency.append((count_of_language, language))
        return sorted(languages_frequency, reverse=True)[:top]


print(most_spoken_languages('../data/countries_data.json', 10))
print(most_spoken_languages('../data/countries_data.json', 3))

# 3
def most_populated_countries(filename, top):
    with open(filename, encoding='utf-8') as file:
        countries_string = file.read()
        countries_data = json.loads(countries_string) # changes this to a list of dictionaries

        # sorting using operator. itemgetter
        sorted_countries = sorted(countries_data, key = operator.itemgetter('population'), reverse=True)
        country_population = []
        for country in sorted_countries:
            country_population.append({'country' : country['name'], 'population': country['population']})
    return country_population[:top]

print(most_populated_countries('../data/countries_data.json', 10))
print(most_populated_countries('../data/countries_data.json', 3))

# Exercises: Level 2
# 4
with open('../data/email_exchanges.txt') as email_exchanges:
    txt =  email_exchanges.read()
    incoming_emails = re.findall('From \S+@\S+', txt) #\S+@\S+ this extracts any group of text with a space between a whitespaces that have the '@'
    incoming_emails = [email[5:] for email in incoming_emails]
    print(incoming_emails)


# 5
def find_most_common_words (filename, top):
    with open(filename) as file:
        txt = file.read()

        # Let's clean the file of any punctuation marks
        clean_txt = re.sub('[^A-Za-z0-9\n ]', '', txt)
        words_list = re.split(r'[ |\n]+', txt)

        # Now, let's do word counts
        words_count = []
        for word in set(words_list):
            word_count = words_list.count(word)
            words_count.append((word_count, word))
    return sorted(words_count,reverse = True)[:top]
print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))


# 6
print(find_most_common_words('../data/obama_speech.txt', 10))
print(find_most_common_words('../data/michelle_obama_speech.txt', 10))
print(find_most_common_words('../data/donald_speech.txt', 10))
print(find_most_common_words('../data/melina_trump_speech.txt', 10))


# Text similarity
# cleaning function
def clean_text (text):
    with open(text) as opened_text:
        txt = opened_text.read()
        removed_punctuation_marks = re.sub('[^A-Za-z0-9\n ]', '', txt)
        return removed_punctuation_marks

def remove_support_words (text):
    words_list = re.split(' |\n', text)
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                  "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                  'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
                  'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
                  'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                  'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
                  'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
                  'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
                  'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
                  'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
                  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
                  "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
                  "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
                  "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
                  'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
                  "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    for word in stop_words:
        if word in words_list:
            words_list.remove(word)
    return words_list

# Jackards similarity analysis
def jackards_similarity(text1, text2):
    transformed_text1 = remove_support_words(clean_text(text1))
    transformed_text2 = remove_support_words(clean_text(text2))
    a = set(transformed_text1)
    b = set(transformed_text2)
    c = a.union(b)
    d = a.intersection(b)
    index = len(d)/len(c)

    return index

print('Jackards similarity index = ', jackards_similarity('../data/michelle_obama_speech.txt', '../data/melina_trump_speech.txt'))


# 8
print(find_most_common_words('../data/romeo_and_juliet.txt', 10))

# 9
import csv
with open('../data/hacker_news.csv', encoding='utf-8') as file:
    opened_file = list(csv.reader(file))
    count = 0

    # Python or python
    for line in opened_file:
        keyword_in_line = False
        for column in line:
            if ('Python' in column) or ('python' in column):
                keyword_in_line = True
        if keyword_in_line == True:
            count = count+1
    print(count)

    # JavaScript, javascript or Javascript
    for line in opened_file:
        keyword_in_line = False
        for column in line:
            if 'javascript' in column.lower():
                keyword_in_line = True
        if keyword_in_line == True:
            count = count+1
    print(count)

    # Java alone
    for line in opened_file:
        keyword_in_line = False
        for column in line:
            if re.search(r'\bjava\b', column.lower()):
                keyword_in_line = True
        if keyword_in_line == True:
            count = count + 1
    print(count)