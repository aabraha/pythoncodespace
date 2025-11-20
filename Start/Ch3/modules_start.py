#
# Working with modules of code

# import the math module, which contains features for working with mathematics
import math
print("The sqaure root of 81 is", math.sqrt(81))
print("The cube root of 27 is", math.cbrt(27))

# import a specific part of the module so you can refer to it more easily
from math import pi
print("PI is equal to", pi)

# import a module and give it a different name
import random as r
print("Random num =", r.randint(100,200))

# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 
print("The mathematical constant e =", math.e)

# Generate a random number between 100 and 200
print("Random num =", r.randint(100,200))

# try some of the math functions for yourself here:
print("The 3 power of 2 is", math.pow(3, 2))

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate
# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
print("\n pipe table format\n")
print(tabulate(data,headers="firstrow", tablefmt="pipe"))
print("\n github table format\n")
print(tabulate(data,headers="firstrow", tablefmt="github"))
print("\n outline table format\n")
print(tabulate(data,headers="firstrow", tablefmt="outline"))
print("\n grid table format\n")
print(tabulate(data,headers="firstrow", tablefmt="grid"))
print("\n simple grid table format\n")
print(tabulate(data,headers="firstrow", tablefmt="simple_grid"))
