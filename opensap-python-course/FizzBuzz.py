"""
Write a Python program that prints the numbers from 1 to 100. If the number is dividable by 3 print Fizz, 
if the number is dividable by 5 print Buzz instead of the number. If the number is dividable by 3 and 5 print FizzBuzz. 
"""

for num in range(1, 101):
    div_3 = False
    div_5 = False

    if num % 3 == 0:
        div_3 = True
    if num % 5 == 0:
        div_5 = True
    
    if div_3 and div_5:
        print("FizzBuzz")
    elif div_5:
        print("Buzz")
    elif div_3:
        print("Fizz")
    else:
        print(num)