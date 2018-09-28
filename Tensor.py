import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Activation
from tensorflow.python.keras.models import Sequential
import numpy as np
from time import sleep
def mutacao(wid):
    aux  = wid
    while (True):
        num = np.random.randint(len(aux))
        if (not hasattr(aux[num], "__len__")):
            aux[num] = np.random.uniform(-1,1)
            break
        aux = aux[num]
    return wid
y = []
for x in range(16):
    if x==0:
        y.append(0.0625)
        continue
    y.append(0.0625 +y[-1]);
y= np.matrix(y)
#print(y)
model = Sequential()
model.add(Dense(32, input_dim=16,kernel_initializer='random_uniform',bias_initializer='random_uniform'))
model.add(Activation('hard_sigmoid'))
model.add(Dense(4,kernel_initializer='random_uniform',bias_initializer='random_uniform'))
model.add(Activation('softmax'))
wid = model.get_weights()
x = model.predict(y)
while True:
    print(model.predict(y))
    wid = mutacao(wid);
    model.set_weights(wid)
    sleep(1)
#print (aux)
#print (wid)

