from turtle import Turtle

class Snake:
    def __init__(self, start_x, color, start_y):
        self.color = color
        self.squares_in_snake = []
        self.starting_x = start_x
        self.starting_y = start_y
        self.create_snake()
        self.head = self.squares_in_snake[0]


    def create_snake(self):

        for i in range(3):
            new_square = Turtle(shape="square")
            new_square.penup()
            new_square.color(self.color)
            new_square.setx(self.starting_x)
            new_square.sety(self.starting_y)
            self.starting_x -= 20
            self.squares_in_snake.append(new_square)

    # the way the snake moves is by replacing the position of the box in front of it. only the first box has a heading
    def move_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)


    def move_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)


    def turn_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)


    def move_snake(self,):



        for square in self.squares_in_snake:
            square.showturtle()



            if square == self.head:
                xcor1 = square.xcor()
                ycor1 = square.ycor()
                square.forward(20)


            else:
                xcor2 = square.xcor()
                ycor2 = square.ycor()
                square.goto(x=xcor1, y=ycor1)
                xcor1 = xcor2
                ycor1 = ycor2

    def increase_snake(self):
        last_x = self.squares_in_snake[-1].xcor()
        last_y = self.squares_in_snake[-1].ycor()
        new_square = Turtle(shape="square")
        new_square.hideturtle()
        new_square.color(self.color)
        new_square.penup()
        self.squares_in_snake.append(new_square)

    def hit_tail(self):
        for square in self.squares_in_snake[1:]:
            if self.head.distance(square) < 10:
                return True

    def reposition(self):
        self.squares_in_snake = self.squares_in_snake[:3]
        self.starting_x = 0
        for square in self.squares_in_snake:
            square.setx(self.starting_x)
            square.sety(self.starting_y)
            self.starting_x -= 20

    def clear_old_snake(self):
        for square in self.squares_in_snake:
            square.hideturtle()

