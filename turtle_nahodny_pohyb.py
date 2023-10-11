from turtle import Turtle, Screen, pensize
import random

tom = Turtle()
tom.shape('turtle')
tom.color('green')
pensize = 1
index = True
while index == True:
    tom.fd(25)
    tom.pensize(pensize)
    b = random.random()
    r = random.random()
    g = random.random()
    angle = (0, 90, 180, 270, 360)
    tom.seth(random.choice(angle))
    tom.pencolor(b, r, g)
    pensize += 0.1
    if pensize >= 5:
        pensize = 5


my_screen = Screen()
my_screen.exitonclick()
