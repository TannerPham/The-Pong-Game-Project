from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
      
    # def create_lpaddle(self):
    #     
    #    
    # def create_rpaddle(self):
    #     self.goto(350, 0)
    # def add_segment(self,position):
    #     new_segment = Turtle(shape="square")
    #     new_segment.color("white")
    #     new_segment.pensize(10)
    #     new_segment.penup()
    #     new_segment.setpos(position)
    #     self.segments.append(new_segment)



    
    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(),new_y)

    def go_down(self):

        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

    # def p2_up(self):
    # 
    #     self.r_segments[0].setheading(90)
    #     self.move(self.r_segments)
    # 
    # def p2_down(self):
    #     self.r_segments[0].setheading(270)
    #     self.move(self.r_segments)
           