import turtle

t = turtle.Turtle()
y = int(input())
m = int(input())
d = [31,28,31,30,31,30,31,31,30,31,30,31]
lis = [['    'for i in range(7)]
       for j in range(6)]

t.penup()
t.goto(350,350)
g=['{}년 {}월'.format(y,m)]
t.write(g,align="right",font=("맑은 고딕",25,"bold"))

l = y - 1
ly = l*365+l // 4-l // 100+l //400

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    d[1] == 29

for i in range(m):
    l +=d[i]


d2 =(ly+1)%7
d3 = 0

for i in range(1,32):
    for j in range(d2,7):
        d3 += 1
        if d3 > d[m]:
            break
    d2=0

w=['   일  월  화  수  목  금   토']
t.penup()
t.goto(45 * i, -45)
t.write(w, align="center", font=("맑은 고딕", 25, "bold"))

for i in range(1,6):
    q=(lis[i][0]+lis[i][1]+lis[i][2]+lis[i][3]+lis[i][4]+lis[i][5]+lis[i][6])
t.penup()
t.goto(-45*i,50)
t.write(q,align="center",font=("맑은 고딕",20,"bold"))

turtle.done()
