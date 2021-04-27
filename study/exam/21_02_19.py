import tensorflow as tf
import numpy as np

t=tf.random.uniform([2,3],0,1)
n=np.random.uniform(0,1,[2,3])
print('tensorflow로 생성한 텐서:\n',t,'\n')
print('numpy로 생성한 ndarray:\n',n,'\n')

res=t+n
print('덧셈 결과:\n',res)

import tensorflow as tf

x=[[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,1.0]]
y=[[-1],[1],[1],[1]]

w=tf.Variable(tf.random.uniform([2,1],-0.5,0.5))
b=tf.Variable(tf.zeros([1]))

opt=tf.keras.optimizers.SGD(learning_rate=0.1)

def forward():
    s=tf.add(tf.matmul(x,w),b)
    o=tf.tanh(s)
    return o

def loss():
    o=forward()
    return tf.reduce_mean((y-o)**2)

for i in range(500):
    opt.minimize(loss,var_list=[w,b])
    if(i%100==0): print('loss at epoch',i,'=',loss().numpy())

o=forward()
print(o)