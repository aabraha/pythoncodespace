
#
# Example file for formatting time and date output
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
currentDatetime = datetime.now()

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(currentDatetime.strftime("The current year is: %Y"))
print(currentDatetime.strftime("The current year is: %y"))

print(currentDatetime.strftime("The current weekday is: %A"))
print(currentDatetime.strftime("The current weekday is: %a"))

print(currentDatetime.strftime("The current month is: %B"))
print(currentDatetime.strftime("The current month is: %b"))

print(currentDatetime.strftime("The current day of month is: %D"))
print(currentDatetime.strftime("The current day of month is: %d"))

print(currentDatetime.strftime("%a, %d %B, %y"))
# %c - locale's date and time, %x - locale's date, %X - locale's time
print(currentDatetime.strftime("Locale date and time: %c"))
print(currentDatetime.strftime("Locale date: %x"))
print(currentDatetime.strftime("Locale time: %X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(currentDatetime.strftime("Current time: %I:%M:%S %p"))
print(currentDatetime.strftime("Current time: %H:%M:%S"))