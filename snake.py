from turtle import Turtle

STARTING_POS = [0,-20, -40]
MOVE_DIST = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        for i in range(3):
            tur = Turtle()
            tur.penup()
            tur.shape("square")
            tur.color("white")
            tur.setx(STARTING_POS[i])
            self.body.append(tur)

    def move(self):
        rev_list = self.body[::-1]

        for idx, part in enumerate(rev_list):
            if idx + 1 < len(self.body):
                part.goto(rev_list[idx + 1].pos())

        self.head.forward(MOVE_DIST)

    def extend(self):
        l = len(self.body)
        tur = Turtle()
        tur.penup()
        tur.goto(self.body[l-1].xcor(), self.body[l-1].ycor())
        tur.shape("square")
        tur.color("white")
        self.body.append(tur)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)