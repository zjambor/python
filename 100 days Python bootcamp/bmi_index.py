from numpy import power


height = int(input("Input your height (cm): "))
weight = float(input("Input your weight (kg): "))
bmi_index = weight / power(height/100, 2)

print(f"Your BMI index is: {bmi_index}")

print(f"Your ideal weight is: {25 * (power(height/100, 2))}")