# importy
from turtle import Turtle, Screen
import random
import turtle

# zmena farebnho kodu
turtle.colormode(255)


# generovanie a nstavenie objektu
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(100)

# funkcia generovania farby
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# kruhy
for number in range(36): # cyklus 1.nahodna farba, 2.otoci sa, 3. smer dolava
    tommy.pencolor(random_color())
    tommy.circle(80)
    tommy.left(10)

my_screen = Screen()
my_screen.exitonclick()
