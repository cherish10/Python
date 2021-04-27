def calc_func(a,b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus() :
        m = x - y
        return m
    return plus, minus

p, m = calc_func(10,20)
print('plus=',p())
print('minus=',m())

class calc_class :
    x = y = 0

    def __init__(self,a,b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10, 20)

print('plus=',obj.plus())
print('minus=',obj.minus())

class Car:
    cc = 0
    door = 0
    carType = None

    def __init__(self, cc, door, carType):
        self.cc = cc
        self.door = door
        self.carType = carType

    def display(self):
        print("자동차는 %d cc이고,문짝은 %d개 타입은 %s" %(self.cc, self.door, self.carType))

car1 = Car(2000,4,"승용차")
car2 = Car(3000, 5, "SUV")

car1.display()
car2.display()

class DatePro:
    content = "날짜 처리 클래스"

    def __init__(self, year, month,day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))


    @classmethod
    def date_string(clscls,dateStr):
        year = dateStr[::4]
        month = dateStr[4::6]
        day = dateStr[6::]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(1995,10,25)
print(date.content)
print(date.year)
date.display()

print(DatePro.content)
DatePro.date_string('199951025')

class Account:
    __balance = 0
    __accName = None
    __accN0 = None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    def getBalance(self):
        return self.__balance,self.__accName, self.__accNo

    def deposit(self, money):
        if money < 0:
            print('잔액 확인')
            return
        self.__balance += money

    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money

acc = Account(1000,'홍길동','125-152-4125-41')

bal = acc.getBalance()
print('계좌정보 : ', bal)

acc.deposit(10000)
bal =  acc.getBalance()
print('계좌정보 : ', bal)

class Super:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('name : %s, age : %d'%(self.name, self.age))

sup = Super('부모',55)
sup.display()

class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print('name : %s, age : %d, gender : %s'%(self.name, self.age, self.gender))

sub = Sub('자식',25,'여자')
sub.display()

class Parent :
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

p = Parent('홍길동','회사원')
p.display()

class Children(Parent):
    gender = None

    def __init__(self, name, job, geder):
        super().__init__(name,job)

        self.gender = geder
    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job,self.gender))

chil = Children("이순신","해군 장군", "남자")
chil.display()

class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print('총 수령액: ',format(self.pay,'3,d'),'원')

class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay*time
        print('총 수령액: ',format(self.pay,'3,d'),'원')

p = Permanent("이순신")
p.pay_calc(3000000,200000)

t = Temporary("홍길동")
t.pay_calc(15000,80)

lst = [1,3,5]
for i, c in enumerate(lst) :
    print('색인 : ',i,end=' ,')
    print('내용: ',c)

dit = {'name':'홍길동','job' : '회사원', 'add': '서울시'}
for i,k in enumerate(dit):
    print('순서 : ',i,end=' ,')
    print('키 : ',k,end=',')
    print('값 :',dit[k])

import datetime
from datetime import date, time

today = date(2019, 10, 23)
print(today)

print(today.year)
print(today.month)
print(today.day)

w = today.weekday()
print('요일 정보: ',w)

currTime = time(21,4,30)
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat()
print(isoTime)

from statistics import mean
from math import sqrt

def Avg(data):
    avg = mean(data)
    return avg

def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)

    return var,sd


from statistics import mean
from math import sqrt

def Avg(data):
    avg = mean(data)
    return avg

def var_sd(data):
    avg = Avg(data)
    diff = [(d- avg) ** 2 for d in data]
    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)
    return var,sd

if __name__ == "__main__":
    data = [1,3,5,7]
    print('평균=',Avg(data))
    var,sd = var_sd(data)
    print('분산=',var)
    print('표준편차=',sd)

from statistics import mean
from math import sqrt



def Avg(data):
    avg = mean(data)
    return avg

def nar_sd(data):
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    return var, sd

data = [1,3,5,7]
print('평균=',Avg(data))
var,sd = var_sd(data)
print('분산=',var)
print('표준편차=',sd)