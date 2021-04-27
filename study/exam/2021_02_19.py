from sklearn import datasets

d = datasets.load_iris()

print(d.DESCR)

for i in range(0,len(d.data)):
    print(i+1,d.data[i],d.target[i])

from sklearn import svm
s = svm.SVC(gamma=0.1,C=10)
s.fit(d.data,d.target)

new_d = [[6.4,3.2,6.0,2.5],[7.3,3.1,4.2,1.35]]

res=s.predict(new_d)
print('새로운 2개 생물의 분류',res)

from sklearn import datasets
import matplotlib.pyplot as plt

digit = datasets.load_digits()

plt.figure(figsize = (5,5))
plt.imshow(digit.images[0],cmap=plt.cm.gray_r,interpolation='nearest')
plt.show()
print(digit.data[0])
print('이 숫자는',digit.target[0],'입니다')

from sklearn import datasets
from sklearn import svm

digit=datasets.load_digits()

s=svm.SVC(gamma=0.1,C=10)
s.fit(digit.data,digit.target)

new_d=[digit.data[0],digit.data[1],digit.data[2]]
res=s.predict(new_d)
print('예측값은',res)
print('참값은',digit.target[0],digit.target[1],digit.target[2])

res=s.predict(digit.data)
correct=[i for i in range(len(res)) if res[i]==digit.target[i]]
accuracy=len(correct)/len(res)
print('화소 특징을 사용했을 때 정확률=',accuracy*100,"%")