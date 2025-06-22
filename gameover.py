from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def show_over(self):
        self.write("Game Over", False, 'center', ("Arial", 24, 'normal'))
