from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1

    def move(self):
        new_x = self.xcor() + 4 * self.x_direction
        new_y = self.ycor() + 4 * self.y_direction
        self.goto(new_x, new_y)

    def change_direction_wall(self):
        self.y_direction *= -1

    def change_direction_paddle(self):
        self.x_direction *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.change_direction_paddle()
        self.change_direction_wall()
