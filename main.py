from turtle import Screen
from paddles import FirstPlayer, SecondPlayer
from line import Line
from ball import Ball, BALL_STARTING_POSITION
from score import ScoreBoard
import time


screen_width = 800
screen_height = 500

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.title("My Pin-Pong Game")
screen.bgcolor("black")
screen.tracer(0)

player_1_name = screen.textinput(title="Player 1", prompt="Enter name: ")
player_2_name = screen.textinput(title="Player 2", prompt="Enter name: ")

ball_x_speed = 5
ball_y_speed = 10

split_screen = Line()
split_screen.draw_line()
player_1 = FirstPlayer()
player_2 = SecondPlayer()
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")

screen.onkeypress(player_2.up, "Up")
screen.onkeypress(player_2.down, "Down")

game_is_on = True

while game_is_on:

    # Ball bouncing off the paddle
    if ball.ball.distance(player_1.paddle) <= 20:
        ball.x_speed -= (ball.x_speed * 2)
        # ball.y_speed -= (ball.y_speed * 2)
        ball.ball.color("red")

    elif ball.ball.distance(player_2.paddle) <= 20:
        ball.x_speed -= (ball.x_speed * 2)
        # ball.y_speed -= (ball.y_speed * 2)
        ball.ball.color("blue")

    # Score update
    if ball.ball.xcor() < -(screen_width / 2):
        ball.ball.goto(BALL_STARTING_POSITION)
        score.player_2_score_update()

    elif ball.ball.xcor() > (screen_width / 2):
        ball.ball.goto(BALL_STARTING_POSITION)
        score.player_1_score_update()

    if score.player_1_score == 10:
        score.player_1_win()
        game_is_on = False
    elif score.player_2_score == 10:
        score.player_2_win()
        game_is_on = False

    screen.update()
    time.sleep(0.001)

    ball.move()

screen.exitonclick()
