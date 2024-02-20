from turtle import Screen, Turtle
from snake import Snake
import time
from snake_food import Food
from resetting_scoreboard import ResettingScoreboard
screen = Screen()
screen.title("Head to Head")
screen.bgcolor("black")
width = 600
height = 400
screen.setup(width=width, height=height)
screen.tracer(0)
screen.listen()
WINNING_SCORE = 1000
DELAY_TIME = 0.3


# Adding blocks
width = int(width / 2)
height = int(height / 2)
for i in range(2):
    x = -1 * width
    if i == 1:
        x = width
    for y in range((-1 * (height - 10)), height + 10, 20):
        block = Turtle(shape="square")
        block.penup()
        block.color("orange")
        block.goto(x, y)

for i in range(2):
    y = -1 * height
    if i == 1:
        y = height
    for x in range((-1 * (width - 10)), (width + 10), 20):
        block = Turtle(shape="square")
        block.penup()
        block.color("orange")
        block.goto(x, y)
# Create snake
snake_1 = Snake(start_x=100, start_y=-100, color="green")
snake_2 = Snake(start_x=-150, start_y=50, color="red")

# Create food
food = Food(x_min=-280, x_max=280, y_min=-180, y_max=180)

# Create scoreboard
scoreboard_1 = ResettingScoreboard(position=(100, 160))
scoreboard_2 = ResettingScoreboard(position=(-100, 160))
scoreboard_1.color("green")
scoreboard_2.color("red")

scoreboard_1.write()
scoreboard_2.write()

# writing winners
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 0)


def red_wins():
    writer.color("red")
    writer.write(arg="THE WINNER IS THE RED SNAKE", align="center", font=("Arial", 20, "normal"))
    screen.update()



def green_wins():
    writer.color("green")
    writer.write(arg="THE WINNER IS THE GREEN SNAKE", align="center", font=("Arial", 20, "normal"))
    screen.update()


green_win = False
red_win = False
game_is_on = True

while game_is_on:
    screen.update()
    snake_1.move_snake()
    snake_2.move_snake()
    time.sleep(DELAY_TIME)
    screen.onkey(fun=snake_1.move_up, key="Up")
    screen.onkey(fun=snake_1.move_down, key="Down")
    screen.onkey(fun=snake_1.turn_right, key="Right")
    screen.onkey(fun=snake_1.turn_left, key="Left")
    screen.onkey(fun=snake_2.move_up, key="w")
    screen.onkey(fun=snake_2.move_down, key="s")
    screen.onkey(fun=snake_2.turn_right, key="d")
    screen.onkey(fun=snake_2.turn_left, key="a")
    if snake_1.head.distance(food) < 15:
        food.refresh()
        snake_1.increase_snake()
        scoreboard_1.update_score()
        DELAY_TIME *= 0.9
    if snake_2.head.distance(food) < 15:
        food.refresh()
        snake_2.increase_snake()
        scoreboard_2.update_score()
        DELAY_TIME *= 0.9

    if scoreboard_1.score == WINNING_SCORE:
        green_wins()
        green_win = True
        game_is_on = False

    if scoreboard_2.score == WINNING_SCORE:
        red_wins()
        red_win = True
        game_is_on = False

    if snake_1.hit_tail() or snake_1.head.xcor() < -290 or snake_1.head.xcor() > 290\
            or snake_1.head.ycor() < -190 or snake_1.head.ycor() > 190:

        red_wins()
        red_win = True
        game_is_on = False

    if snake_2.hit_tail() or snake_2.head.xcor() < -290 or snake_2.head.xcor() > 290\
            or snake_2.head.ycor() < -190 or snake_2.head.ycor() > 190:
        green_wins()
        green_win = True
        game_is_on = False

    for parts in snake_2.squares_in_snake:
        if snake_1.head.distance(parts) < 10:
            red_wins()
            red_win = True
            game_is_on = False

    for parts in snake_1.squares_in_snake:
        if snake_2.head.distance(parts) < 10:
            green_wins()
            green_win = True
            game_is_on = False

    if green_win and red_win:
        writer.clear()
        writer.write(arg="IT IS A TIE", align="center", font=("Arial", 20, "normal"))

screen.exitonclick()
