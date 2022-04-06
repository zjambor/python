from ast import Constant
import random
import turtle as t
from turtle import Screen

ANGLE = 360

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.penup()
tim.goto(-200,50)
tim.pendown()

def draw_shape(_angle, _num_sides):
    for s in range(3, _num_sides):
        tim.color(random.choice(colours))
        for _ in range(s):
            tim.forward(100)
            tim.right(_angle / s)

num_sides = 11
draw_shape(ANGLE, num_sides)

t.mainloop()