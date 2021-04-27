import turtle
from turtle import Screen,Turtle

t = Turtle("turtle")
screen = Screen()
t.speed(0)
t.pensize(10)


def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def clickRight():
    t.clear()

screen.listen()
t.ondrag(dragging)
turtle.onscreenclick(clickRight,3)
screen.mainloop()