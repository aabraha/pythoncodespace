# 
# Example file for complex types

# Sequences: Lists , Tuples and Sets
# These are -- surprise -- sequences of values
myList = [0, 1, "two", 3.5, False]
# print(len(myList))
# to access a member of a sequence type, use []
# print(myList[2])
# print(myList[-1])
# myList[0] = 10
# print(myList)
#print(myList[:-1])

# add a list to another list
# anotherList = [6, 7, 8]
# print(myList + anotherList)
# # a string is an immutable char list
# myStr = "This is a string"
# print(myStr[2])

# use slices to get parts of a sequence
# print(myList)
# print("Sliced [1,4] ->", myList[1:4])
# print("Sliced [1,4,2] ->", myList[1:4:2]) # start = index 1, end = index 3, step amount=2
# print("Sliced default [::] ->", myList[::])
# print("Sliced [::2] ->", myList[::2]) # default start: 0, default end: last index, step=2

# you can use slices to reverse a sequence
# print("Reverse a list [::-1] ->", myList[::-1])

# Tuples are like lists, but they are immutable
myTuple = (0, 1, 2, "three")
# print(myTuple)
# print(myTuple[1])
# myTuple[1] = "one" # you can't change the values

# Sets are also sequences, but they contain unique values
mySet = {1, 2, 3, 2, "hey"}
# print(mySet) # only holds unique values
# Set, however, can not be indexed like lists or tuples
# print(mySet[0]) # this will cause an error

# Test for membership
print(1 in myList)
print(3 in myTuple)
print(5 in mySet)
