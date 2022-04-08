import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

tim.speed(12)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(10):
    tim.penup()
    tim.goto(-300, -150 + (i * 40))
    tim.pendown()
    for _ in range(10):
        
        tim.fillcolor(random_color())  
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()

        tim.penup()
        tim.forward(40)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()