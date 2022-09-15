from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 55, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 170)
        self.color("white")
        self.player_1_score = 0
        self.player_2_score = 0
        self.write(arg=f"{self.player_1_score} {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def player_1_score_update(self):
        self.clear()
        self.player_1_score += 1
        self.write(arg=f"{self.player_1_score} {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def player_2_score_update(self):
        self.clear()
        self.player_2_score += 1
        self.write(arg=f"{self.player_1_score} {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def player_1_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Player 1 Win!", align=ALIGNMENT, font=FONT)

    def player_2_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Player 2 Win!", align=ALIGNMENT, font=FONT)



