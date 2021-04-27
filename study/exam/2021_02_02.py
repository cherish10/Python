chartset = ['abc','red','green','yellow','blue','black','abc','yellow','sugar','cream','blue','abc','sugar']
wc = {}

for key in chartset :
    wc[key] = wc.get(key,0) + 1
print(wc)

import random

dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

vmax = vmin = dataset[5]

for i in dataset:
    if vmax < i:
        vmax = i
    if vmin >i :
        vmin = i

print('max =',vmax,'min=',vmin)

dataset = [5,10,18,22,35,55,75,103]
value = int(input("검색할 값 입력:"))

low = 0
high = len(dataset) -1
loc = 0
state =False

while (low <= high):
    mid = (low + high) //2

    if dataset [mid] > value:
        high = mid - 1
    elif dataset[mid] < value:
        low = mid + 1
    else:
        loc = mid
        state = True
        break
if state:
    print('찾는 위치 : %d 번쨰' %(loc+1))
else:
    print('찾는 값은 없습니다')


position = ['과장','부장','대리','사장','대리','과장']
wc = {}

s = set(position)
l = list(s)

for n in position:
    wc[n] = wc.get(n,0)+1

print('중복되지 않은 직위:',l)
print('각 직위별 빈도수:',wc)

dataset = list(range(1,6))
print(dataset)

print('len=',len(dataset))
print('sum=',sum(dataset))
print('max=',max(dataset))
print('min=',min(dataset))

import statistics
print('평균=',statistics.mean(dataset))
print('중위수=',statistics.median(dataset))

from statistics import variance,stdev

print("표준 분산=",variance(dataset))
print("표본 표준편차=",stdev(dataset))

def userFunc3(x,y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

x = int(input('x 입력 : '))
y = int(input('y 입력 : '))

t, s, m, d = userFunc3(x,y)
print('tot=',t)
print('sub=',s)
print('mul=',m)
print('div=',d)

from statistics import mean,variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

def Avg(data):
    avg = mean(data)
    return avg

print('산술평균=',Avg(dataset))

def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

v,s= var_sd(dataset)
print('분산=', v)
print('표준편차=', s)

def coin(n) :
    result = []
    for i in range(n):
        r = random.randint(0,1)
        if (r == 1) :
            result.append(1)
        else:
            result.append(0)
    return result
print(coin(10))

def montaCoin(n) :
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0]

    result = cnt / n
    return result
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))

