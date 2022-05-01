"""
Triangles can be classified based on their angles.

    A right triangle has one angle of 90°
    A obtuse triangle has one angle of more than 90°
    A triangle is acute if all three angles are less than 90°

Write a program that asks the user for the values of three angles in degrees. 
First check if the entered values are valid. The values are only valid if they are >0 and if their sum is 180°. 
If the entered values are valid, classify the triangle as right, acute or obtuse.
"""

angle1 = int(input("Please enter the first angle: "))
angle2 = int(input("Please enter the second angle: "))
angle3 = int(input("Please enter the third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    if (angle1 + angle2 + angle3) == 180:
        print("The triangle is a right triangle.")
    else:
        print("The entered values are not valid.")
else:
    print("Angles smaller than 0 are not valid.")