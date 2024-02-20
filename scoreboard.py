from turtle import Turtle
with open("data.txt") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.hideturtle()
        self.goto(position)
        self.pencolor("yellow")
        self.penup()

    def write(self,):
        super().write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Courier", 14, "normal"))

    def update_score(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.clear()
        self.write()

    def end_score(self, end_pos):
        self.goto(end_pos)
        super().write(arg="GAME OVER", align="center", font=("Arial", 30, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()

