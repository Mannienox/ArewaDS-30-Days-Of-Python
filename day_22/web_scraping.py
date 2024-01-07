# Exercises: Day 22
# 1
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

all_elements = soup.find_all()

all_elements_list = [str(element) for element in all_elements]


data = {
    'url': url,
    'content': all_elements_list
}

with open('scraped_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# 2
url = 'https://archive.ics.uci.edu/ml/datasets.php'  # link is broken. It's showing 404

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
print(len(tables))
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)


# 3
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
presidents_table = soup.find('table', {'class': 'wikitable'})

presidents_data = []


if presidents_table:
    rows = presidents_table.find_all('tr')[1:]
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 5:
            number = columns[0].text.strip()
            name = columns[3].text.strip()
            term = columns[4].text.strip()


            president_info = {
                'number': number,
                'name': name,
                'term': term
            }
            presidents_data.append(president_info)


with open('presidents.json', 'w') as json_file:
    json.dump(presidents_data, json_file, indent=4)

