import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.y = -250
        self.x = 0
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=0.7)
        self.color("white")
        self.penup()
        self.setpos(self.x, self.y)

    def move_right(self):
        if self.x >= 400:
            self.x = -400
        self.x = self.x + 40
        self.setpos(self.x, self.y)

    def move_left(self):
        if self.x <= -400:
            self.x = 400
        self.x = self.x - 40
        self.setpos(self.x, self.y)
