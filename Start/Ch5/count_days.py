# Count the number of instances of a particular weekday in a given month/year

# You're given a month and a year, along with a day of the week (Monday through Sunday).

# Your task: Return the number of instances of that day of the week in the given month.

# Parameters

# year: Four-digit year

# month: Two-digit month

# whichday: Number of the weekday (0 is Monday, 6 is Sunday)

# Result

# int: The number of times the given weekday occurs within the specified month

# Constraints

# The year and month values are always valid calendar values.

# The whichday argument is always 0 through 6, inclusive.

# Example 1

# Input: 2025, 12, 0 (December 2025, Monday)
# Result: 5 (There are five Mondays in December 2025.)

# Example 2

# Input: 2030, 1, 5 (January 2030, Saturday)
# Result: 4 (There are four Saturdays in January 2030.)
import calendar

def countDays(year, month, whichDay):
  counter = 0
  listWeek = calendar.monthcalendar(year, month)
  for week in listWeek:
    if week[whichDay] != 0:
      counter += 1
  return counter

# Test method
year = int(input("Enter the year(yyyy):"))
month = int(input("Enter the month(1...12):"))
day = int(input("Enter which day you would like to count(0...6):"))

print(f"There are {countDays(year, month, day)} {calendar.day_name[day]}s in {calendar.month_name[month]} {year}")