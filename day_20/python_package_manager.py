# Exercises: Day 20
# 1
import requests
import re
'''url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt' # I used the above link cos the link in the question is broken
txt = requests.get(url).text

clean_txt = re.sub('[^A-Za-z0-9\n ]', '', txt)
words_list = re.split(r'[ |\n|\r]+', txt)

# Now, let's do word counts
words_count = []
for word in set(words_list):
    word_count = words_list.count(word)
    words_count.append((word_count, word))
print(sorted(words_count, reverse=True)[:10])'''

# 2
# i
import statistics
url = 'https://api.thecatapi.com/v1/breeds'
breeds = requests.get(url).json()
metric_units = []
for breed in breeds:
    print(breed)
    metric_units.append(breed['weight']['metric'])

# computations
# getting class marks
end_points = []
for element in metric_units:
    end_points.append(re.findall('[\d]+', element))
print(end_points)

class_mark = []
list_of_endpoints = []
for elm in end_points:
    k, v = elm
    class_mark.append((int(k)+int(v))/2)
    list_of_endpoints.append(int(k))
    list_of_endpoints.append(int(v))
print('Details for weight in Metric Units')
mn = min(list_of_endpoints)
print('min = ', mn)
mx = max(list_of_endpoints)
print('max = ', mx)
mean = statistics.mean(class_mark)
print('mean = ', mean)
median = int(statistics.median(class_mark))
print('median = ', median)
std = statistics.stdev(class_mark)
print('standard deviation = ', std)

# ii
lifespan = []
for breed in breeds:
    lifespan.append(breed['life_span'])

# computations
# getting class marks
end_points = []
for element in lifespan:
    end_points.append(re.findall('[\d]+', element))
print(end_points)


class_mark = []
list_of_endpoints = []
for elm in end_points:
    k, v = elm
    class_mark.append((int(k)+int(v))/2)
    list_of_endpoints.append(int(k))
    list_of_endpoints.append(int(v))
print('\n\nDetails for weight in Metric Units')
mn = min(list_of_endpoints)
print('min = ', mn)
mx = max(list_of_endpoints)
print('max = ', mx)
mean = statistics.mean(class_mark)
print('mean = ', mean)
median = int(statistics.median(class_mark))
print('median = ', median)
std = statistics.stdev(class_mark)
print('standard deviation = ', std)

# iii
country_code = []
for breed in breeds:
    if 'country_code' in breed:
        country_code.append(breed['country_code'])
    else:
        country_code.append(breed['country_codes'])

print('\n\nCountry\t\tNumber of breeds')
for x in set(country_code):
    print(x, '\t\t\t',country_code.count(x))


# 3
# i
url = 'https://restcountries.com/v3.1/all'
countries_data = requests.get(url).json()
countries_data_list = []
for country in countries_data:
    countries_data_list.append((country['area'], country['name']['common']))

print('Top 10 largest countries by area of land: ')
for country in sorted(countries_data_list, reverse=True)[:10]:
    area, name = country
    print('\t',name,'\t\t\t',area)


# ii
languages = []
count = 0
for country in countries_data:
    if 'languages' in country:
        for language in country['languages'].values():
            languages.append(language)
    elif 'language' in country:
        for language in country['language'].values():
            languages.append(language)
    else:
        count = country['name']['common']
print(count)
language_count = []
for language in set(languages):
    language_count.append((languages.count(language), language))

print('The 10 most spoken languages:  ')
for language in sorted(language_count, reverse=True)[:10]:
    count, lang = language
    print('\t',lang,'\t\t\t',count)

# iii
print('The total number of languages in the languages api is', len(set(languages)))


# iv
url = 'https://archive.ics.uci.edu/datasets'
from bs4 import BeautifulSoup
from pprint import pprint

site = requests.get(url).text
print(site)
my_list = []
html = BeautifulSoup(site, 'html.parser')
