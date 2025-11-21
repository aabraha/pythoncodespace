# Python code​​​​​​‌‌‌​‌​‌​​​‌‌‌‌​‌‌‌​‌​​‌​​ below
# Use print("messages...") to debug your solution.
def is_palindrome(teststr):
    # Your code goes here.
    if len(teststr) == 0: 
        return False
    if len(teststr) == 1:
        return True
    # make sure the string only contains alphanumeric
    # listFiltered = []
    newStr = ""
    for ch in teststr:
        if ch.isalnum():
            # listFiltered.append(ch)
            newStr += ch
    #convert lsit of char into a string
    # strFiltered = "".join(listFiltered)
    # convert the string into lower case
    strLowercase = newStr.lower()
    # use string slice to reverse the string and compare with the original to determine whether it's a palindrome
    strReversed = strLowercase[::-1]
    return strLowercase == strReversed

test_word = "Madam, I'm Adam."
# try using some of these other words:
test_word2 = "RACE CAR!"
test_word3 = "Hello, world"
test_word4 = "Radar?"
test_word5 = "A man, a plan, a canal Panama!"

print(is_palindrome(test_word))
print(is_palindrome(test_word2))
print(is_palindrome(test_word3))
print(is_palindrome(test_word4))
print(is_palindrome(test_word5))

