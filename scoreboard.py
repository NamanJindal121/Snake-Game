from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 275)
        self.color('white')
        self.write("Score: 0", False, 'center', ('Arial', 15, 'normal'))
        self.speed('fastest')
        self.hideturtle()
        self.score = 0

    def updateScore(self):
        self.score +=1
        self.clear()
        self.write("Score: "+str(self.score), False, 'center', ('Arial', 15, 'normal'))

