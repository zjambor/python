# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
val = int(age) / 3
print(float(val))
print(int(val))
#Write your code below this line 👇
print(round(val))
print(f"your score is {val} and it is {True}")

left_for_90 = 90 - int(age)
print(f"You have {left_for_90*365} days, {left_for_90*53} weeks, and {left_for_90*12} months left for 90")

print("Welcome to the tip calculator")
total = float(input("What was the toltal bill? "))
percent = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
pay = total * (1 + percent / 100) / people
final_amount = "{:.2f}".format(round(pay,2))
print(f"Each person should pay: {final_amount}")