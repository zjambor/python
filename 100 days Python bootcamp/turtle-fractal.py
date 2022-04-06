import turtle as t
from turtle import Screen

tim = t.Turtle()

tim.penup()
tim.goto(-200,50)
tim.pendown()

tim.getscreen().bgcolor("black")
tim.color("green")
tim.speed(12)

def star(size):
    if size > 10:
        for _ in range(5):
            tim.forward(size)
            star(size / 3)
            tim.left(216)

star(360)

t.mainloop()