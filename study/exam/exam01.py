var = int(input('짐의 무게는 얼마입니까'))
if var>=10:
    susu = (var//10)*10000
    print('수수료는'+format(susu)+'입니다')

else:
    print('수수료는 없습니다')


import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1,10)

while True:
    my = int(input('에상 숫자를 입력하세오:'))

    if my==com:
        print('~~성공~~')
        break
    elif my<com:
        print('더 큰 수 입력')
    elif my>com:
        print('더 작은 수 입력')

a = 0
print('수열 =',end=' ')

for n in range(1,101):
    if n %3==0 and n %2!=0:
        print(n,end=' ')
        a+=n
print()
print('누적합= %d'%a)

string="""안녕하세요. 파이썬 세계로 오시니걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

words=[]
for word in string.split():
    words.append(word)
for s in words:
    print(s)

print('단어 개수:',len(words))



l = []

while len(l) != 6:
    a = random.randint(1, 45)
    if a not in l:
        l.append(a)

l.sort()

userNum = []
while len(userNum) <6:
    num = int(input("%d 번쨰 숫자를 입력하세요:" %(len(userNum)+1)))
    if num in userNum:
        print("이미 입력된 숫자입니다 다른번호 입력하세요")
    else:
        if num > 0 and num <46:
            userNum.append(num)
        else:
            print("1~45까지의 숫자를 입력하여 주세요")
userNum.sort()

print('컴퓨터가 뽑은 숫자-',l)
print('사람이 뽑은 숫자',userNum)

matchingCount = 0
for num in userNum:
    if num in l:
        matchingCount += 1

print('일치하는 숫자의 수-',matchingCount)

if var == 6:
    print('1등')
elif var == 4:
    print('3등')
elif var == 3:
    print('4등')
elif var == 2:
    print('5등')
else:
    print('꽝')

