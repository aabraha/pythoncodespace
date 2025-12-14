#
# Example file for working with Calendars
#


import calendar

# create a plain text calendar
textCalendar = calendar.TextCalendar(calendar.SUNDAY)
#print(textCalendar.formatyear(2025))
janMonth = textCalendar.formatmonth(2025,1)
print("The month January is:\n", janMonth)

textCalendar = calendar.TextCalendar(calendar.MONDAY)
janMonth = textCalendar.formatmonth(2025,1)
print("The month January is:\n", janMonth)

# create an HTML formatted calendar
htmlCalendar = calendar.HTMLCalendar(calendar.SUNDAY)
janMonth = htmlCalendar.formatmonth(2025,1)
#print("Html month Jan is:\n", janMonth)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month(s)
print("August 2026 month is:\n",textCalendar.formatmonth(2026,8))
for i in textCalendar.itermonthdays(2026,8):
  print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("Calendar month names:")
for monthName in calendar.month_name:
  print(monthName)
print("Calendar day names:")
for dayName in calendar.day_name:
  print(dayName)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("########## Team meetings of the year will be on: ##############")
for month in range(1,13):
  listWeek = calendar.monthcalendar(2026,month)
  weekOne = listWeek[0]
  weekTwo = listWeek[1]

  if weekOne[calendar.FRIDAY] != 0:
    meetingDay = weekOne[calendar.FRIDAY]
  else:
    meetingDay = weekTwo[calendar.FRIDAY]

  print(f"{calendar.month_name[month]} : {meetingDay} {calendar.day_name[calendar.FRIDAY]} ")
