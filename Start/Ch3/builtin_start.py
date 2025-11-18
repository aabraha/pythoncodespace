# python is "battries included" language
# Example file for using built-in functions
#

myString = "The quick, brown fox jumped over the lazy dog!"
myNumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
print("length of myString:",len(myString))
print("length of myNumber:",len(myNumbers))

# the max() and min() functions will find the largest and smallest value in a sequence
print("the max of myString", max(myString))
print("the min of myNumber:", min(myNumbers))

# the str() function will return a string version of an object
prefix = "result: "
result = 5
# print(prefix + result)
print(prefix + str(result))


# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
print("range of numbers")
for i in range(5,15): # exluding the stop value
  print(i)

print("range of numbers with step value")
for i in range(5, 15, 2):
  print(i)

print("iterate through a string char")
for i in range(5, len(myString), 2):
  print(myString[i])

# the print function itself is pretty flexible - you can embed variables directly in it
# interpolated 
greeting = "Hello!"
count = 10
print("interpolated strings")
print(f"{greeting} you are visitor number {count}")
