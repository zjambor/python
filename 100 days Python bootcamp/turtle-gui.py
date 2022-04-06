import turtle as t
from turtle import Screen

tim = t.Turtle()

tim.penup()
tim.goto(-200,50)
tim.pendown()

for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

t.clearscreen()

tim.getscreen().bgcolor("black")
tim.color("green")
tim.speed(12)

for r in range(20):
    tim.circle(-1 * (r * 5 + 10))

t.mainloop()