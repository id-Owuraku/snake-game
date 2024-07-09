from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   Highscore:{self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                self.highscore = self.score
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  Highscore:{self.highscore}", align=ALIGNMENT, font=FONT)
