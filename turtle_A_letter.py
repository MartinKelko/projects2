import turtle

# Create a turtle object
t = turtle.Turtle()

# Move turtle to the starting position
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw letter "A"
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(40)
t.right(105)
t.forward(45)

# Hide turtle
t.hideturtle()

# Keep the window open until it is closed manually
turtle.done()
