from turtle import Turtle

STARTING_POSITION_X = 0
STARTING_POSITION_Y = -230
STARTING_POSITIONS = (STARTING_POSITION_X, STARTING_POSITION_Y)

LINE_HEIGHT = 15
SCREEN_HEIGHT = 250
NUMBER_OF_LINES = int(SCREEN_HEIGHT / LINE_HEIGHT)


class Line:
    def __init__(self):
        self.line = Turtle()
        self.line.color("white")
        self.line.pensize(5)
        self.line.penup()
        self.line.hideturtle()
        self.line.speed("fastest")
        self.line.left(90)
        self.move_line()

    def move_line(self):
        self.line.goto(STARTING_POSITIONS)

    def draw_line(self):
        for lines in range(NUMBER_OF_LINES):
            self.line.pendown()
            self.line.forward(LINE_HEIGHT)
            self.line.penup()
            self.line.forward(LINE_HEIGHT)
