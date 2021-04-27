import turtle

turtle = turtle.Turtle()

turtle.color("#FF0000")
turtle.shape("turtle")
turtle.speed(0)
screen = turtle.getscreen()
turtle.penup()
s = '*방항키이동,o:원,z:지우기,c:색변경,r:사각형,q:종료'
turtle.write(s,align="right",font=("맑은 고딕",15,"bold"))

def left():
    turtle.left(30)
def right():
    turtle.right(30)

def up():
    turtle.forward(30)
def down():
    turtle.forward(30)

def circle():
    turtle.circle(30)

def undo():
    turtle.undo()

def space():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

def endProgram():
    screen.bye()

def colour():
    turtle.color("#0100FF")

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(circle,"o")
screen.onkeypress(undo,"z")
screen.onkeypress(space,"space")
screen.onkeypress(endProgram,"q")
screen.onkeypress(colour,"c")
screen.onkeypress(square,"r")
screen.listen()
screen.mainloop()

