from turtle import Turtle

FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):        
        self.goto(0, 270)
        self.write("Score: " + str(self.score), True, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=FONT)