import numpy as np
a=np.array([1,2,3])
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)

a = np.array([1,2,3],dtype='int32')
b = np.array([1,2,3],dtype='int64')
print(a.dtype)
print(b.dtype)
c = a + b
print(c.dtype)

a = np.array([1,'two',3])
print(a)

a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a)
b = np.array(range(10))
print(b)
c = np.array(range(0,10,2),dtype='int64')
print(c)

print(c.shape)
print(c.ndim)
print(c.dtype)
print(c.size)
print(c.itemsize)

a = np.array([1,2,3])
print(a.max())
print(a.min())
print(a.mean())

a = np.array([[1,1],[2,2],[3,3]])
print(a.flatten())

a = np.array([1,2,3])
b = np.array([[4,5,6],[7,8,9]])
print(np.append(a,b))
print(np.append([a],b,axis=0))

array = np.random.randint(10,size=(5,3))
print(array)

array = np.sum(array,axis=0)
print(array)

array3 = np.random.randint(10,size=(5,3,2))
print(array3)
print(np.sum(array3,axis = 0))

print('-----')
a = np.array([23,45,7,30,34,82])
print('최대값:',a.max())
print('최소값:',a.min())
print('평균:',a.mean())

b = np.random.randint(0,100,size =10)
print(b)
print('최대값:',b.max())
print('최소값:',b.min())
print('평균:',b.mean())

c = np.append(a,b)
print(c)

print('-----')
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)

print(np.matmul(a,b))
print(a @ b)

print(np.linspace(0,10,5))
print(np.linspace(0,10,4))

a1 = np.full((3,3),2)
print(a1)

a2 = np.arange(1,13)
print(a2)

a3 = np.arange(0,50,3)
print(a3)

a1 = np.arange(1,13).reshape(2, 6)
print(a1)

a2 = np.arange(1,31).reshape(3, 10)
print(a2)

a= np.array([1,3,4])
print(np.insert(a,1,2))

a = np.array([[1,1],[2,2],[3,3]])
print(np.insert(a,1,4,axis=0))

print(np.insert(a,1,4, axis = 1))

a = np.random.randint(1,101,size=15).reshape(3,5)
print('a =',a)
print('a 의 열방향 최대값:',a.max(axis=0))
print('a 의 열방향 최소값:',a.min(axis=0))
print('a 의 열방향 평균:',a.mean(axis=0))
print('a 의 행방향 최대값:',a.max(axis=1))
print('a 의 행방향 최소값:',a.min(axis=1))
print('a 의 행방향 평균:',a.mean(axis=1))

a_list = [10,20,30,40,50,60,70,80]
print(a_list[1:5])

a = np.array([10,20,30,40,50,60,70,80])
print(a[1:5])
print(a[1:])
print(a[:])
print(a[::2])
print(a[::-1])

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print('b=',a[1:9:2])
print('b=',a[5:])
print('c=',a[6:])
print('d=',a[:3])
print('e=',a[0::2])
print('f=',a[::-2])

