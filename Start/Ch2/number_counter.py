#Python code below
# Use print("messages...") to debug your solution.

def count_numbers(which, numbers):
    # Your code goes here
    counter = 0;
    if which == "even":
        for num in numbers:
           if num % 2 == 0:
                counter+=1
        return counter
    elif which =="odd":
        for num in numbers:
            if num % 2 != 0:
                counter += 1
        return counter
    
    return -1

# This is how your code will be called.
# You can edit this code to try different testing cases.
numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

result1 = count_numbers("even", numbers)
print("even numbers:", result1)
result2 = count_numbers("odd", numbers)
print("odd numbers:", result2)
result3 = count_numbers("Blarg", numbers)
print("invalid word:", result3)