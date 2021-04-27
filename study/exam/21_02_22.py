'''
a = int(input('첫번째 숫자를 입력: '))
b = int(input('두번째 숫자를 입력: '))

if a < b:
    b,a = a,b
for i in range(a,(a * b )+1):
    if i % a == 0 and i % b == 0:
        print('최소공배수:', i)
        break
'''

'''
simsa = int(input())
vote = input()[:simsa]
if vote.count("A") > vote.count("B"):
    print("A")
else:
    print("B")
#aCount, bCount = 0

#for i in range(simsa):
#    if "A" in vote:
#        aCount +=1
#    elif "B" in vote:
#        bCount +=1

#if aCount > bCount:
#    print("A")
#elif a < b:
#    print("B")
#else:
#    print("Tie")
'''

# s = int(input('참여수:'))
#
# for sang in range(s):
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     a = [x,y,z]
#
#     if x == y == z :
#         sang = 10000 + (x)*1000
#         print(sang)
#
#     elif x == y or x == z:
#         sang = 1000 + (x)*100
#         print(sang)
#
#     elif y == z:
#         sang = 1000 + (y) * 100
#         print(sang)
#
#     else :
#         sang = max(a)*100

# from collections import Counter
#
# price = []
# for i in range(int(input())):
#     a,b,c = input().split(" ")
#     dice = [a,b,c]
#
#     count = Counter(dice)
#     print(count)
#
#     if 3 in count.values():
#         num = int(list(count.keys())[0])
#         price.append(10000 + num + 1000)
#
#     elif 2 in count.values():
#         print(sorted(count,key=count.get,reverse=True))
#         num = int((sorted(count,key=count.get,reverse=True)[0]))
#         price.append(10000 + num + 100)
#     else :
#         price.append(int(max(dice)) + 100)
#
# print(max(price))

n = int(input())
a = set(n)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

