from turtle import Turtle

class Mainscreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.shape("square")
        self.hideturtle()
    def draw_border(self):
        #draw the dashed line in betwenn
        self.goto(0,300)
        self.setheading(270)
        self.pensize(10)
        for _ in range (7):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.forward(60)
        for _ in range (7):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        # draw the upper and lower walls
        self.setheading(0)
        self.penup()
        self.goto(-350,320)
        self.pendown()
        self.forward(700)
        self.penup()
        self.goto(-350, -320)
        self.pendown()
        self.forward(700)
        # draw the circle in the middle
        self.penup()
        self.pensize(5)
        self.goto(0,-28)
        self.pendown()
        self.circle(30)