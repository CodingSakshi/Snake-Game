from turtle import Turtle

FONT = "Arial, 15, bold"
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('score.txt', 'r') as file:
            self.high_score = int(file.read()) 
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
