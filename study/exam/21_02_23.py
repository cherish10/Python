# T = int(input())
#
# if T % 10 == 0 :
#     a = T // 300
#     T = T % 300
#
#     b = T // 60
#     T = T % 60
#
#     c = T // 10
#     T = T % 10
#     print(a,b,c)
#
# else :
#     print('-1')

import turtle

t = turtle.Turtle()

y = int(input())
m = int(input())
d = [0,31,28,31,30,31,30,31,31,30,31,30,31]
lis = [['    'for i in range(7)]
       for j in range(6)]


y1=y-1
l = y1*365+y1//4-y1//100+y1//400

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    d[2] == 29

for i in range(m):
    l +=d[i]

d2 =(l+1)%7
d3 = 0

for i in range(1,32):
    for j in range(d2,7):
        d3 += 1
        if d3 > d[m]:
            break
        lis[i][j]='%4d'%d3
    d2=0

print('{}년 {}월'.format(y,m))
print('-'*28)
print('   일  월  화  수  목  금   토')
for i in range(1,6):
    print(lis[i][0]+lis[i][1]+lis[i][2]+lis[i][3]+lis[i][4]+lis[i][5]+lis[i][6]+'\n')

t.penup()
t.goto(45 * i, -45)
t.write(lis, align="center", font=("맑은 고딕", 25, "bold"))
turtle.done()