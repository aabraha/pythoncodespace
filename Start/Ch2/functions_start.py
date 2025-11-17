# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def helloFunc():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)
#helloFunc() #using the func defined

# function that takes parameters
def helloFunc(greetings):
  print("hello world!")
  name = input("What is your name? ")
  print(greetings, name)

# helloFunc("How are you doing")
# helloFunc("What's up")

# function that returns a value
def cube(x):
  return x*x*x
result = cube(3)
# print("the cube value is",result)

# function with default value for a parameter
def helloFunc(greetings, name=None):
  print("hello world!")
  if name == None:
    name = input("What is your name? ")
  print(greetings, name)

# helloFunc("Nice to meet you", "Assefa") 
# helloFunc("Nice to meet you") 
# helloFunc(name = "Abraha", greetings="Nice to meet you") 


# function with variable number of parameters
def multiAdd(*args):
  result = 0
  for x in args:
    result += x
  return result

# print(multiAdd(4,5,10,4,10))

# the variable param should be at the end of params
def multiAddParams(start, *args):
  result = 0
  for x in args:
    result += x
  return result * start

print(multiAddParams(10, 4,5,10,4,10))