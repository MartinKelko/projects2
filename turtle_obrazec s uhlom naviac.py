from turtle import Turtle
import random

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)

colors = ["red","gold", "green"]
moves = 3

while moves != 9:
    random_color = random.choice(colors)
    tommy.pencolor(random_color)
    for _ in range(moves):
        tommy.forward(100)
        tommy.right(360/moves)
    moves += 1

for _ in range(3):
    tommy.forward(100)
    tommy.right(120) # 360 stupnov / 3 strany trojuholnika

for _ in range(4):
    tommy.forward(100)
    tommy.right(90) #360 stupnov / 4 strany obdlznika

for _ in range(5):
   tommy.forward(100)
   tommy.right(72) #360 stupnov / 5 stran patuholnika
    
my_screen = Screen()
my_screen.exitonclick()
