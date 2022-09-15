from turtle import Turtle

STARTING_POSITIONS = [(-370, 0), (370, 0)]

PADDLE_SPEED = 40

SCREEN_HEIGHT_POSITIVE = 220
SCREEN_HEIGHT_NEGATIVE = -220


class FirstPlayer:
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=3)
        self.paddle.left(90)
        self.paddle.speed("fastest")
        self.paddle.color("white")
        self.move_paddle_to_start()

    def move_paddle_to_start(self):
        self.paddle.penup()
        self.paddle.goto(STARTING_POSITIONS[0])

    def up(self):
        if self.paddle.ycor() < SCREEN_HEIGHT_POSITIVE:
            self.paddle.forward(PADDLE_SPEED)

    def down(self):
        if self.paddle.ycor() > SCREEN_HEIGHT_NEGATIVE:
            self.paddle.backward(PADDLE_SPEED)


class SecondPlayer(FirstPlayer):
    def __init__(self):
        super().__init__()
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=3)
        self.paddle.goto(STARTING_POSITIONS[1])





