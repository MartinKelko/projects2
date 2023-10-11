from turtle import Turtle, Screen

arrow1 = Turtle("arrow")
arrow2 = Turtle("arrow")
arrow1.color("red")
arrow2.color("green")
arrow1.pensize(2)
arrow2.pensize(2)
arrow1.circle(20)

for i in range(30,80,10):
    print(i)
    arrow2.circle(i)
    

my_screen = Screen()
my_screen.exitonclick()
