import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Activation
from tensorflow.python.keras.models import Sequential
import numpy as np
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
model.add(Dense(4))
model.add(Activation('softmax'))
#print (model.get_weights())
x = model.predict(y)
print (x)
print(x.argmax())
