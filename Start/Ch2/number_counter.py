#Python code below
# Use print("messages...") to debug your solution.

def count_numbers(which, numbers):
    # Your code goes here
    counter = 0
    if which != "even" and which != "odd":
        return -1
    for num in numbers:
        if which == "even" and num % 2 == 0:
            counter+=1
        
        if which =="odd" and num % 2 != 0:
            counter += 1
    return counter


# This is how your code will be called.
# You can edit this code to try different testing cases.
numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

result1 = count_numbers("even", numbers)
print("even numbers:", result1)
result2 = count_numbers("odd", numbers)
print("odd numbers:", result2)
result3 = count_numbers("Blarg", numbers)
print("invalid type input:", result3)