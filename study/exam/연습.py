'''
누진세 코드
전기사용량 >500) 기본요금 =9330; 전기시용요금 = 전기사용량 * 494.0;
전기사용량 >400) 기본요금 =5103; 전기시용요금 = 전기사용량 * 274.3;
전기사용량 >300) 기본요금 =2710; 전기시용요금 = 전기사용량 * 184.3;
전기사용량 >200) 기본요금 =1130; 전기시용요금 = 전기사용량 * 127.8;
전기사용량 >100) 기본요금 =660; 전기시용요금 = 전기사용량 * 88.5;
전기사용량 <100) 기본요금 =330; 전기시용요금 = 전기사용량 * 52;

세금 = (기본요금 + 전기사용요금) *0.09
이번달사용요금 = 기본요금 + 전기 사용요금 + 세금
이번달사용요금은???입니다.
'''

'''
a = int(input('a='))
b = int(input('b='))

if a>b:
    b,a = a,b

lst = list(range(a,b+1))
result = sum(lst)
print(result)
'''

arr = [1,1,1,3,3,5,5,5]
s = []

for d in arr :
    if s[-1] != [d]:
        s.append(d)

print(s)