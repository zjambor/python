from turtle import Turtle
from pathlib import Path

FONT = ('Arial', 18, 'normal')
HOME = str(Path.home()) + "/"     # os.path.expanduser('~')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(HOME + "data.txt", "r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):        
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()        

    def reset(self):        
        if self.score > self.high_score:
            self.high_score = self.score
        with open(HOME + "data.txt", "w") as data:
            data.write(str(self.high_score))
        self.score = 0        
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, align="center", font=FONT)