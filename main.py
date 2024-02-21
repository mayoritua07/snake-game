import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()

screen.setup(width=500, height=400)
i = 0
color_list = ["red", "green", "blue", "orange", "purple", "yellow"]
turtle_list = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]
for item in turtle_list:
    item.color(color_list[i])
    item.pencolor(color_list[i])
    item.shape("turtle")
    item.speed(2)
    i += 1


x = -250
y = 150

for item in turtle_list:
    item.penup()
    item.setposition(x, y)
    y -= 50

choice = screen.textinput(title="Turtle Race voting", prompt="type the color of the turtle you believe would win")
play = True
while play:

    for item in turtle_list:
        item.speed(10)
        distance = random.randint(1, 10)
        item.forward(distance)

    for item in turtle_list:
        if item.xcor() >= 240:
            play = False

position = 0
for item in turtle_list:
    if item.xcor() > position:
        position = item.xcor()
        winner = item
if choice == winner.pencolor():
    print(f"You were right, The {winner.pencolor()} turtle is the winner")
else:
    print(f"you were wrong, The {winner.pencolor()} turtle is the winner")

screen.exitonclick()

# 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