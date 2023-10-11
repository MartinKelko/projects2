from turtle import Turtle

tommy = Turtle()
tommy.shape("turtle")

for _ in range(5):
    tommy.pendown()
    tommy.forward(20)
    tommy.penup()
    tommy.forward(20)

my_screen = Screen()
my_screen.exitonclick()
