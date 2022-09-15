from turtle import Turtle

SCREEN_WIDTH_POSITIVE = 400
SCREEN_WIDTH_NEGATIVE = -400
SCREEN_HEIGHT_POSITIVE = 250
SCREEN_HEIGHT_NEGATIVE = -250

BALL_STARTING_POSITION = (0, -200)


class Ball:
    def __init__(self):
        self.ball = Turtle("square")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.ball.penup()
        self.ball.goto(BALL_STARTING_POSITION)
        self.x_speed = 5
        self.y_speed = 5

    def move(self):
        self.ball.setx(self.ball.xcor() - self.x_speed)
        self.ball.sety(self.ball.ycor() + self.y_speed)

        # Bouncing
        if self.ball.ycor() >= SCREEN_HEIGHT_POSITIVE:
            self.y_speed -= (self.y_speed * 2)

        elif self.ball.ycor() <= SCREEN_HEIGHT_NEGATIVE:
            self.y_speed -= (self.y_speed * 2)
