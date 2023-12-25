# Exercises: Day 16

# 1
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f'Date: {day}/{month}/{year}, Time: {hour}:{minute} Timestamp: {timestamp}')

# 2
time_now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(time_now)

# 3
today_string = '5 December, 2019'
formatted_today_string = datetime.strptime(today_string, "%d %B, %Y")
print(formatted_today_string)

# 4
from datetime import date
new_year = datetime(2024,1,1)
diff = new_year - now
print(f'{diff} left to NEW YEAR')

# 5
then = datetime(1970,1,1)
diff = now - then
print(f'From 1 January, 1970, we had {diff}')

# 6
'''
1. We can use it for time analysis
2. We can use it to get timestamp of any activities in an application
3. Adding posts on a blog
4. For creating fun apps like an app to compute how long you have lived on earth in seconds, minutes, hours, weeks, months and years
5. For working on time stamps in data analysis
6. For extracting and formatting time from timestamps in data analysis
'''