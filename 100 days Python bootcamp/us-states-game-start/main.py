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
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# states_to_learn = []

# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)

states_to_learn = [state for state in all_states if state not in guessed_states]

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv()

# with open('states_to_learn.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     csvwriter.writerow(states_to_learn)

screen.mainloop()

# screen.exitonclick()
