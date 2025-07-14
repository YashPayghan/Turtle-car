from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def create_score(self):
        self.goto(-230, 250)
        self.color("black")
        self.write(f"level: {self.level}", align="center", font=FONT)

    def increse_level(self):
        self.level += 1
        self.clear()
        self.create_score()

    def game_over(self):
        self.color("black")
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)