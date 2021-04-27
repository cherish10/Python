def Func1(name, *names):
    print(name)
    print(names)


Func1("홍길동", "이순신", "유관순")

from statistics import mean, variance ,stdev

def statis(func, * data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TyperError'

print('avg=', statis('avg',1,2,3,4,5))
print('var=', statis('var',1,2,3,4,5))
print('std=', statis('std',1,2,3,4,5))

def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동',35, addr='서울시', height= 175,weight=65)

x = 50
def local_func(x):
    x += 50
local_func(x)
print('x=',x)

def global_func():
    global x
    x += 50

global_func()
print('x=',x)

def a() :
    print('a 함수')
    def b():
        print('b 함수')
    return b
b = a()
b()

data = list(range(1,101))
def outer_func(data):
    dataSet = data
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot=',tot_val)
avg_val = avg(tot_val)
print('avg=',avg_val)

from statistics import mean
from math import sqrt

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

def scattering_func(data):
    dataSet = data

    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    def var_func(avg):
        diff = [ (data - avg) **2 for data in dataSet]
        print(sum(diff))
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func

avg,var,std = scattering_func(data)

print('평균: ', avg())
print('분산: ', var(avg()))
print('표준편차: ', std(var(avg())))

def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal  num_val
        num_val = value

    return getter, setter

getter, setter = main_func(100)

print('num=',getter())
setter(200)
print('num=',getter())

def wrap(func):
    def decorated() :
        print("방가워료")
        func()
        print("잘가요")
    return decorated

@wrap
def hello() :
    print('hi~ 홍길동')

hello()