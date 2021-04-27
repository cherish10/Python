class Rectangle:
    width = 0
    height = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return area
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 :'))
h = int(input('사각형의 세로 입력 :'))

r = Rectangle(w,h)
area = r.area_calc()

print('사각형의 넓이:',w)
circum = r.circum_calc()
print('사각형의 둘레:',h)

from statistics import mean
from math import sqrt

x = [5,9,1,7,4,6]

class Scattering:
    def __init__(self,data):
        self.data = data

    def var_func(self):
        avg = mean(self.data)
        diff = [(a - avg) ** 2 for a in x]
        var = sum(diff) / (len(x)-1)
        print('분산:', var)
        return var

    def ste_func(self,var):
        st = sqrt(self.var)
        print('표준편차:',str)

str = Scattering(x)
str.ste_func(str.var_func())


class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        if self.gender == 'female':
            self.gender = '여자'
        else:
            self.gender = '남자'

print('이름: %s ''나이: %d' %(self.name,age))

name = input('이름: ')
age = int(input('나이:'))
gender = input('성별(male/female):')

p = Person(age, name, gender)
p = display()

class Employee:
    name = None
    pqy = 0

    def __init__(self,name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pqy_calc(self, base, bonus):
        self.pqy = base + bonus
        print('급여:',format(self.pqy,'3,d'))

class Temporary(Employee):
    def __init__(self,name):
        super().__init__(name)

    def pay_calc(self, tpay,time):
        self.pqy = tpay * time
        print('급여:',format(self.pqy,'3,d'))

empType = input("고용형태 선택(정규직<P>, 임시직<T> : ")
if empType == 'P' or empType == 'p':
    name = input('이름 : >?')
    base = int(input('기본급 : >?'))
    bonus = int(input('상여금 : >?'))
    print("="*20)
    print('고용형태 : 정규직')
    emp = Permanent(name,base,bonus)
    emp.pay_calc()

elif empType == 'T' or empType == 't':
    name = input('이름 : >?')
    time = int(input('작업시간 : >?'))
    tpay = int(input('시급 : >?'))
    print("=" * 20)
    print('고용형태 : 임시직')
    emp = Permanent(name, time, tpay)
    emp.pay_calc()

else :
    print('='*30)
    print('입력오류')
name = input('이름: ')