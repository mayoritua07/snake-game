import time
from turtle import Screen, Turtle
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard


def restart_game():
    my_scoreboard.clear()
    my_scoreboard.score = 0
    my_snake.clear_old_snake()





screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
delay_time = 0.20

    # adding blocks to the side of the screen

for i in range(2):
    x = - 300
    if i == 1:
        x = 300
    for y in range(-290, 310, 20):
        block = Turtle(shape="square")
        block.penup()
        block.color("orange")
        block.goto(x, y)


    for i in range(2):
        y = - 300
        if i == 1:
            y = 300
        for x in range(-290, 310, 20):
            block = Turtle(shape="square")
            block.penup()
            block.color("orange")
            block.goto(x, y)


food = Food(x_min=-280, y_min=-280, x_max=280, y_max=280)
my_scoreboard = Scoreboard(position=(0, 270))
i_want_to_play = True
while i_want_to_play:
    my_snake = Snake(start_x=0, start_y=0, color="white")
    screen.listen()
    my_scoreboard.setposition(0, 270)
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(delay_time)
        my_snake.move_snake()
        screen.onkey(fun=my_snake.move_up, key="Up")
        screen.onkey(fun=my_snake.turn_left, key="Left")
        screen.onkey(fun=my_snake.move_down, key="Down")
        screen.onkey(fun=my_snake.turn_right, key="Right")
        my_scoreboard.write()

    #     detecting collision with food
        if my_snake.head.distance(food) < 15:
            food.refresh()
            my_scoreboard.score += 100
            my_scoreboard.update_score()
            my_snake.increase_snake()
            if delay_time != 0.05:
                delay_time -= 0.01/2

        if my_snake.hit_tail():
            game_is_on = False
            my_scoreboard.reset()
            time.sleep(1)

        if my_snake.head.xcor() >= 290 or my_snake.head.xcor() <= -290:
            game_is_on = False
            my_scoreboard.reset()
            time.sleep(1)

        if my_snake.head.ycor() >= 290 or my_snake.head.ycor() <= -290:
            game_is_on = False
            my_scoreboard.reset()
            time.sleep(1)

        if not game_is_on:
            restart = screen.textinput(title="Do you want to play again", prompt="Type yes to play again or no to end")
            if restart and restart.lower() == "yes":
                restart_game()
            else:
                i_want_to_play = False

screen.exitonclick()
