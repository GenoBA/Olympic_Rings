import turtle
screen = turtle.Screen()
screen.screensize(1000, 500)
screen.bgcolor('tan')

t = turtle.Turtle()
t.penup()

#blue circle
t.goto(-80,15)
t.pencolor('blue')
t.pendown()
t.circle(35)
t.penup()

#black circle
t.goto(0,15)
t.pencolor('black')
t.pendown()
t.circle(35)
t.penup()

#red circle
t.goto(80,15)
t.pencolor('red')
t.pendown()
t.circle(35)
t.penup()

#yellow circle
t.goto(-40,-15)
t.pencolor('yellow')
t.pendown()
t.circle(35)
t.penup()

#green circle
t.goto(40,-15)
t.pencolor('green')
t.pendown()
t.circle(35)
t.penup()


#text 1
t.goto(0,100)
t.pencolor('purple')
t.write("Winter Olympics",font=("Arial",30, "bold"), align="center")

#text 2
t.goto(0,-100)
t.write("2026",font=("Arial",30, "bold"), align="center")


turtle.done()
