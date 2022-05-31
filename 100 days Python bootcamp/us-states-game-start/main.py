# import turtle
from turtle import Screen, Turtle
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

if answer_state in all_states:
    t = Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())

screen.mainloop()

# screen.exitonclick()
