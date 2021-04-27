s = {1,3,4,2,3,4}
print(len(s))
print(s)

for d in s:
    print(d,end=' ')
print()

s2 = {1,5}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

s3 = {1,3,4}
print(s3)

s3.add(7)
print(s3)


s3.discard(3)
print(s3)

gender = ['남','여','남','여']

sgender = set(gender)
lgender = list(sgender)
print(lgender)

print(lgender[1])

dic = dict(key1 = 100, key2 =200, key3 = 300)
print(dic)

person = {'name':'홍길동','age':'35', 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic),type(person))

person['age'] = 45
print(person)

del person['address']
print(person)

person['pay'] = 350
print(person)
