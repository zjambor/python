"""
Using the library random create 10,000 random points inside the square. That means generate 10,000 random pairs of values for x and y. 
The random value must be between 0 and 1 in order for a point to be inside the square. For each point check if x² + y² is < 1. 
If this is the case, then the point is within the circle. 
Count the total number of points and the points which are in the circle. Use these numbers to calculate π. 
Finally compare your calculated value of π with the value of π found in the math library. 
Do this by printing the calculated value of π, the value from the math library as well as the difference.

Below is an example execution of the program. Note that your values might be different.

Calculated value of π: 3.1396
Value of π from math library: 3.141592653589793
Difference: -0.0019926535897929476
"""

import random
import math

NUM_OF_POINTS = 10000
# circle_points = 0

# for _ in range(NUM_OF_POINTS):
#     x, y = random.random(), random.random()     # random number between 0 and 1
#     if (x**2 + y**2) < 1:
#         circle_points += 1

points = [(random.random(), random.random()) for _ in range(NUM_OF_POINTS)]

# circle_points = [x for x in points if (x[0]**2 + x[1]**2) < 1]
circle_points = list(filter(lambda x: (x[0]**2 + x[1]**2) < 1, points))

CALC_PI = len(circle_points) / (NUM_OF_POINTS / 4)

print("Calculated value of π:", CALC_PI)
print("Value of π from math library:", math.pi)
print("Difference:", CALC_PI - math.pi)

##### second version
# works only with NUM_OF_POINTS < 1000

def points_in_the_circle(list_of_points, circle_points_):
    if list_of_points != []:
        # act_element = list_of_points[0]
        # tail = list_of_points[1:]
        act_element, *tail = list_of_points

        if (act_element[0]**2 + act_element[1]**2) < 1:
            circle_points_.append(act_element)
        points_in_the_circle(tail, circle_points_)
    return circle_points_

if NUM_OF_POINTS <= 900:
    CP = len(points_in_the_circle(points, []))
    print(CP)

    CALC_PI = CP / (NUM_OF_POINTS / 4)

    print("Calculated value of π:", CALC_PI)
    print("Value of π from math library:", math.pi)
    print("Difference:", CALC_PI - math.pi)
