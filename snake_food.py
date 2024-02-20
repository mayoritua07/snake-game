from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, x_min, x_max, y_min, y_max):
        super().__init__()
        self.x_max = x_max
        self.y_max = y_max
        self.x_min = x_min
        self.y_min = y_min
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(self.x_min, self.x_max)
        random_y = random.randint(self.y_min, self.y_max)
        self.goto(random_x, random_y)

