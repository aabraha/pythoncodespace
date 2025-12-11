#
# Example file for working with date information

from datetime import date #imports date class from datetime module
from datetime import datetime #imports datetime class from datetime module

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print("Today's date is", today)

# print out the date's individual components
print("Date components", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's weekday #:", today.weekday())
days = ["mon","tue","wed","thu","fri","sat","sun"]
print("Which is ", days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
todayDateAndTime = datetime.now()
print("Today's date and time is", todayDateAndTime)

# Get the current time
time1 = datetime.time(datetime.now())
time2 = datetime.time(todayDateAndTime)
print("The current time is", time1)
print("The current time is", time2)