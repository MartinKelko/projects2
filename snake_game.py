#importy
from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("green")
screen.title("Vitajte v hadej hre")
screen.setup(width=600, height=600)
screen.tracer(False) #zakomentuj

#hadia hlava a jablko
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

body_parts = []

#funkcie
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if  head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if  head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if  head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#funkcie
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

#aktivacia klavesov
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

#hlavny cyklus 
while True:
    screen.update()

    #kontrola kolizie s hranoou platna obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"

        #skryjeme casti tela
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)

        #vyprazdnimecasti tela (sede stvorceky)
        body_parts.clear()

        
    if head.distance(apple) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x,y)

        #Pridanie casti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

    move()

    #hlava narazila do tela
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            
            #skryjeme casti tela
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)

            #vyprazdnime  casti tela (sede stvorceky)
            body_parts.clear()
    
    time.sleep(0.1)
    
screen.exitonclick()



































