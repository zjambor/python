def palindrome(text):
    text = text.lower()
    return text[::-1] == text
    
print(palindrome("Racecar"), palindrome("24742"), palindrome("24789"))

def palindrome2(text):
    text = text.lower()
    return "".join(reversed(text)) == text

text="palindrome"
print("".join(reversed(text)))

print(palindrome2("Racecar"), palindrome2("24742"), palindrome2("24789"))

"""
Implement the function is_even(number) which gets an integer as input parameter and checks, 
if this input is even or not. is_even() will return the boolean value True if the value is even and False if the input is not even.

Implement a for loop which iterates over the range(100). Within the for loop, 
the sequence-variable is checked with the function is_even(). Depending on the return value, 
either x is even or x is not even is printed.
"""

def is_even(num):
    return num % 2 == 0

for i in range(1, 101):
    if is_even(i): 
        print(f"{i} is even")
    else: 
        print(f"{i} is not even")