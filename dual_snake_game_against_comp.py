from turtle import Screen, Turtle
from snake import Snake
import time
from snake_food import Food
from resetting_scoreboard import ResettingScoreboard


screen = Screen()
screen.title("PYTHON SNAKE: first to seven wins")
screen.bgcolor("black")
width = 1200
height = 600
screen.setup(width=width, height=height)
screen.tracer(0)
screen.listen()
DELAY_TIME = 0.15
WINNING_SCORE = 700

# Adding blocks to the screen
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

for y in range((-1 * (height - 10)), height + 10, 20):
    x = 0
    block = Turtle(shape="square")
    block.penup()
    block.color("orange")
    block.goto(x, y)

# Adding snakes
r_snake = Snake(start_x=300, start_y=0, color="white")
l_snake = Snake(start_x=-300, start_y=0, color="white")

# Adding Food
r_food = Food(x_min=20, x_max=570, y_min=-280, y_max=280)
l_food = Food(x_min=-570, x_max=-20, y_min=-280, y_max=280)

# Adding scores
r_scoreboard = ResettingScoreboard(position=(300, 260))
l_scoreboard = ResettingScoreboard(position=(-300, 260))

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("yellow")


r_scoreboard.write()
l_scoreboard.write()
game_is_on = True
l_snake_move = True
r_snake_move = True
left = 0

while game_is_on:
    screen.update()
    time.sleep(DELAY_TIME)
    if r_snake_move:
        r_snake.move_snake()
    if l_snake_move:
        if l_snake.head.ycor() - l_food.ycor() > 10 or l_snake.head.ycor() - l_food.ycor() < -10:
            if l_snake.head.ycor() < l_food.ycor() and left == 0:
                l_snake.move_up()

                left += 1

            elif l_snake.head.ycor() > l_food.ycor() and left == 0:
                l_snake.move_down()

                left += 1

            elif left == 0 and l_snake.head.ycor() > 250:
                l_snake.turn_left()

            elif left == 0 and l_snake.head.ycor() < -250:
                l_snake.turn_left()

        if l_snake.head.ycor() - l_food.ycor() < 10 or l_snake.head.ycor() - l_food.ycor() > - 10:
            if l_snake.head.xcor() < l_food.xcor() and left == 0:
                l_snake.turn_right()

                left += 1
            if l_snake.head.xcor() > l_food.xcor() and left == 0:
                l_snake.turn_left()

                left += 1

            elif left == 0 and l_snake.head.xcor() > -50:
                l_snake.move_up()

            elif left == 0 and l_snake.head.xcor() < -550:
                l_snake.move_up()

        l_snake.move_snake()

    screen.onkey(fun=r_snake.move_up, key="Up")
    screen.onkey(fun=r_snake.move_down, key="Down")
    screen.onkey(fun=r_snake.turn_right, key="Right")
    screen.onkey(fun=r_snake.turn_left, key="Left")

    if r_snake.head.distance(r_food) < 15:
        r_food.refresh()
        r_scoreboard.update_score()
        r_snake.increase_snake()
        DELAY_TIME *= 0.9

    if l_snake.head.distance(l_food) < 15:
        l_food.refresh()
        l_scoreboard.update_score()
        l_snake.increase_snake()

    if l_snake.hit_tail() or l_snake.head.xcor() < -590 or l_snake.head.xcor() > -10 or l_snake.head.ycor() < -290\
            or l_snake.head.ycor() > 290:
        l_snake_move = False

    if r_snake.hit_tail() or r_snake.head.xcor() > 590 or r_snake.head.xcor() < 10 or r_snake.head.ycor() < -290 or\
            r_snake.head.ycor() > 290:

        r_snake_move = False

    if not r_snake_move and not l_snake_move:
        game_is_on = False

    if l_scoreboard.score == r_scoreboard.score and l_scoreboard.score == WINNING_SCORE:
        writer.goto(0, 0)
        r_snake.move_snake()
        l_snake.move_snake()
        screen.update()
        writer.write(arg="IT IS A TIE", align="center", font=("Arial", 30, "normal"))

    elif r_scoreboard.score == WINNING_SCORE:
        writer.goto((300, 0))
        r_snake.move_snake()
        screen.update()
        writer.write(arg="YOU WIN", align="center", font=("Arial", 30, "normal"))
        writer.goto((-300, 0))
        if l_snake_move:
            writer.write(arg="YOU LOSE", align="center", font=("Arial", 30, "normal"))
        game_is_on = False

    elif l_scoreboard.score == WINNING_SCORE:
        writer.goto((-300, 0))
        l_snake.move_snake()
        screen.update()
        writer.write(arg="YOU WIN", align="center", font=("Arial", 30, "normal"))
        writer.goto((300, 0))
        if r_snake_move:
            writer.write(arg="YOU LOSE", align="center", font=("Arial", 30, "normal"))
        game_is_on = False
    left = 0

    if not l_snake_move:
        writer.clear()
        writer.goto((-300, 0))
        writer.write(arg="YOU LOSE", align="center", font=("Arial", 30, "normal"))
        writer.goto((300, 0))
        writer.write(arg="YOU WIN", align="center", font=("Arial", 30, "normal"))
        game_is_on = False

    if not r_snake_move:
        writer.clear()
        writer.goto((300, 0))
        writer.write(arg="YOU LOSE", align="center", font=("Arial", 30, "normal"))
        writer.goto((-300, 0))
        writer.write(arg="YOU WIN", align="center", font=("Arial", 30, "normal"))
        game_is_on = False




screen.exitonclick()
