import turtle

t=turtle.Turtle()
t.penup()
c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x=0
y=0

for i in range(0, len(c)):
    if i % 7 == 0:
        x = 0
        y = y + 1
    else:
        x = x + 1

    t.goto(45 * x,-45 * y)
    t.write(c[i], align="right",font=("맑은 고딕",20,"bold"))

turtle.done()

