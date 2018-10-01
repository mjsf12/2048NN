from __future__ import print_function
import numpy as np
import mxnet as mx
from mxnet import nd, autograd, gluon
from random import SystemRandom
data_ctx = mx.cpu()
model_ctx = mx.cpu()

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
    def __init__(self, **kwargs):
        super(mydence, self).__init__(**kwargs)

    def get_wid(self):
        pass

    def set_wid(self):
        pass

    def get_bias(self):
        pass
    
    def set_bias(self):
        pass

        

class Rede(gluon.Block):
    def __init__(self,**kwargs):
        super(Rede,self).__init__(**kwargs)
        with self.name_scope():
            self.dense1=gluon.nn.Dense(32,use_bias=True,weight_initializer=uniform_de_verdade(),bias_initializer=uniform_de_verdade(),in_units=16)
            self.dense2= gluon.nn.Dense(4,use_bias=True,weight_initializer=uniform_de_verdade(),bias_initializer=uniform_de_verdade())

    def forward(self,x):
        print(x)
        x=self.dense1(x)
        print(x)
        x=nd.sigmoid(x)
        print(x)
        x=self.dense2(x)
        print(x)
        x=nd.softmax(x)
        print(x)
        return x
        
rd = Rede()
rd.collect_params().initialize(mx.init.Normal(sigma=.01), ctx=model_ctx)
data = nd.ones((1,16))
#rd(data.as_in_context(model_ctx))
#print(rd.dense1.__dict__.keys())
#print(vars(rd.dense1.bias['_data']))
print(rd.dense1.save_params())
#rd(data.as_in_context(model_ctx))