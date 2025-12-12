#
# Example file for working with timedelta objects
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=7, minutes=20))

# print today's date
currentDatetime = datetime.now()
print("Current date and time is ", currentDatetime)

# print today's date one year from now
print("In one year from now it will be: ", currentDatetime + timedelta(days=365))

# create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be: ",currentDatetime + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
weekAgo = currentDatetime - timedelta(weeks=1)
weekAgoFormated = weekAgo.strftime("%A %B %d, %Y")
print("A week ago it was:", weekAgoFormated)

### How many days until April Fools' Day?
today = date.today()
aprilFoolDay = date(today.year, 4, 1)
if aprilFoolDay < today:
  print(f"April fool's day already went by {(today - aprilFoolDay).days} days ago")
  aprilFoolDay = aprilFoolDay.replace(year=today.year + 1)

timeToAprilFoolDay = aprilFoolDay - today
print(f"It's just {timeToAprilFoolDay.days} days until the next april fool's day")