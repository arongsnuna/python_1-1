import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
win.setup(800,600)

t1.penup()
t1.goto(-200,100)
t1.pendown()
t1.goto(200,100)
t1.penup()
t1.goto(-200,-100)
t1.pendown()
t1.goto(200,-100)
t1.penup()
t1.goto(-80,100)
t1.pendown()
t1.goto(-80,-100)
t1.penup()
t1.goto(80,100)
t1.pendown()
t1.goto(80,-100)

win.exitonclick()
