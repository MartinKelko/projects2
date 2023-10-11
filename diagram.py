from turtle import Turtle, Screen
import random
import turtle

tommy = Turtle()
tommy.shape("arrow")

barvy = ("purple", "red", "yellow", "green", "blue", "pink")

delka = 2

for x in range(10):
    for i in range(6):
        tommy.pencolor(barvy[i])
        tommy.forward(delka)
        tommy.left(60)
        delka += 1

screen = Screen()
screen.exitonclick()
