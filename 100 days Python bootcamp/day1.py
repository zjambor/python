# Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("hello" + " " + "Angela")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#print("Hello " + input("What is your name? "))

#print(len(input("What is your name? ")))

s = input("What is your name? ")

print(s + " hossza: " + str(len(s)))

# 🚨 Don't change the code below 👇
a = int(input("a: "))
b = int(input("b: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# tmp = a
# a = b
# b = tmp

a = a + b
b = a - b
a = a - b

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + str(a))
print("b: " + str(b))

#1. Create a greeting for your program.
print("Wlecome to the Brand Name Generator\n")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city where you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
brand_name = city + " " + pet
print("Your band name could be: " + brand_name + "\n\n")
