import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

tim.penup()
tim.goto(-200,50)
tim.pendown()
tim.speed(12)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

size_of_gap = 10

for r in range(int(360 / size_of_gap)):
    tim.color(random_color())   
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

screen = t.Screen()
screen.exitonclick()