# Find the longest string in a list of strings
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def find_largest(stringList):
    # Your code goes here
    maxLen = 0
    for str in stringList:
        if maxLen < len(str):
            maxLen = len(str)

    return maxLen

# This is how your code will be called.
# Your answer should be the length of the longest string in the list
# You can edit this code to try different testing cases.
test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
result = find_largest(test_strings)
print(f"the longest string has a length of {result} chars")