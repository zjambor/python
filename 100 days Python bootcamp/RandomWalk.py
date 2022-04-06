from ast import Constant
import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

tim.penup()
tim.goto(-200,50)
tim.pendown()
tim.speed(10)
tim.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    tim.setheading(random.choice(directions))
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)

t.mainloop()