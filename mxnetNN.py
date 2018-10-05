from __future__ import print_function
import numpy as np
import mxnet as mx
from mxnet import nd, autograd, gluon
from random import SystemRandom
from time import sleep


class uniform_de_verdade(mx.initializer.Initializer):
    def __init__(self,**kwargs):
        super(uniform_de_verdade,self).__init__(**kwargs)

    def _init_bias(self,a,b):
        i = b.shape[0]
        for x in range(i):
            b[x] = np.random.uniform(-1,1)

    def _init_weight(self,a,b):
        if b.ndim == 1:
            i = b.shape[0]
            for x in range(i):
                b[x] = np.random.uniform(-1,1)
        else:
            i,j = b.shape
            for x in range(i):
                for y in range(j):
                    b[x][y] = np.random.uniform(-1,1)

class mydence(gluon.nn.Dense):

    def get_wid(self):
        return self.weight._data

    def set_wid(self,weight):
        self.weight._data = weight

    def get_bias(self):
        return self.bias._data
    
    def set_bias(self,bias):
        self.bias._data = bias


        

class Rede(gluon.Block):
    def __init__(self,**kwargs):
        super(Rede,self).__init__(**kwargs)
        with self.name_scope():
            self.dense1=mydence(64,use_bias=True,weight_initializer=uniform_de_verdade(),bias_initializer=uniform_de_verdade(),in_units=16)
            self.dense2=mydence(4,use_bias=True,weight_initializer=uniform_de_verdade(),bias_initializer=uniform_de_verdade(),in_units=64)
        self.data_ctx = mx.cpu()
        self.model_ctx = mx.cpu()
        self.collect_params().initialize(mx.init.Normal(sigma=.01), ctx=self.model_ctx)

    def forward(self,x):
        x=self.dense1(x)
        x=nd.relu(x)
        x=self.dense2(x)
        x=nd.softmax(x)
        return x

    def get_wids(self):
        return self.dense1.get_wid(),self.dense2.get_wid()

    def get_bias(self):
        return self.dense1.get_bias(),self.dense2.get_bias()
    
    def set_bias(self,bias1,bias2):
        self.dense1.set_bias(bias1)
        self.dense2.set_bias(bias2)

    def set_wid(self,weight1,weight2):
        self.dense1.set_wid(weight1)
        self.dense2.set_wid(weight2)

    def predict(self,x):
        x = nd.array(x)
        x=x.reshape((1,16))
        x= x/nd.max(x)
        Y = self(x.as_in_context(self.model_ctx))
        return (Y.argmax(axis=1))

    def get_genes(self):
        w1,w2 = self.get_wids()
        b1,b2 = self.get_bias()
        return [w1,b1,w2,b2]

    def set_genes(self,gene):
        self.set_wid(gene[0],gene[2])
        self.set_bias(gene[1],gene[3])

        
        
# rd = Rede()
# data = nd.ones((1,16))
# rd.predict(data)
# b1,b2 = rd.get_bias()
# w1,w2 = rd.get_wids()
# b1=bo.mutacao(b1)
# b2=bo.mutacao(b2)
# w1=bo.mutacao(w1)
# w2=bo.mutacao(w2)
# rd.set_bias(b1,b2)
# rd.set_wid(w1,w2)
# rd.predict(data)
