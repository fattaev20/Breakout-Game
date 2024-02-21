import time
import turtle
from turtle import Screen
import paddle
import ball
import block

game_is_on = True

screen = Screen()
screen.title("Breakout in Turtle")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("white")
text.goto(-100, 200)

p = paddle.Paddle()
b = ball.Ball()
blocks = []

y_pos = 120
for i in range(4):
    x_pos = -380
    for j in range(18):
        bl = block.Block()
        bl.goto(x_pos, y_pos)
        if i % 2 == 0:
            bl.color("red")
        x_pos = x_pos + 44
        blocks.append(bl)

    y_pos = y_pos - 24

screen.listen()
screen.onkeypress(p.move_right, "Right")
screen.onkeypress(p.move_left, "Left")

while game_is_on:
    screen.update()
    if b.ycor() <= -290:
        text.write("Game over!", font=("Helvetica", 30, "normal"))
        game_is_on = False

    if b.get_distance(p) < 45 and b.ycor() <= -235:
        b.bounce_y()
    for bl in blocks:
        if b.distance(bl) < 30:
            bl.hideturtle()
            blocks.remove(bl)
            b.bounce_y()
    b.move()
    time.sleep(0.05)

screen.mainloop()
