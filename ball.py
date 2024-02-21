import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = -200
        self.y_step = 10
        self.x_step = 10
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)

    def move(self):
        self.bounce()
        self.x, self.y = self.x + self.x_step, self.y + self.y_step
        self.goto(self.x, self.y)

    def bounce(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_step = self.y_step * (-1)
        if self.xcor() >= 390 or self.xcor() <= -390:
            self.x_step = self.x_step * (-1)

    def bounce_y(self):
        self.y_step = self.y_step * (-1)

    def get_distance(self, turtle):
        return self.distance(turtle)
