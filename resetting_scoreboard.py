from turtle import Turtle


class ResettingScoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(position)
        self.pencolor("yellow")
        self.penup()

    def write(self, *kwargs):
        super().write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", 14, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write()

    def end_score(self, end_pos):
        self.goto(end_pos)
        super().write(arg="GAME OVER", align="center", font=("Arial", 30, "normal"))

    def reset(self):
        self.score = 0
        self.update_score()

