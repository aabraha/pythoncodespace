# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10/0
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
  x=10/0
except:
  print("Division by zero didn't work!")

# You can also catch specific exceptions
try:
  input = input("Enter a num to divide 10 by:")
  num = int(input)
  print(10/num)
except ZeroDivisionError as e:
  print("Division by zero error.\n",e)
except ValueError as e:
  print(f"Invalid input. '{input}' \n{e}")
finally:
  print("Finally always runs to gracefully handle resources")

