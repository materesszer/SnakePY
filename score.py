from turtle import Turtle


class Score:
    """Score display in upper left corner"""

    def __init__(self):
        self.score = 0
        self.score_display = self.setup_score_display()
        self.update_score_display()

    @staticmethod
    def setup_score_display():
        display = Turtle()
        display.hideturtle()
        display.penup()
        display.color("white")
        display.goto(-290, 270)
        return display

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(
            f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score_display()
