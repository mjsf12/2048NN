from mxnetNN import Rede
from mxnet import nd, autograd, gluon
from BO import BO
from time import sleep
bo =BO()
data = nd.ones((1,16))
r1 = Rede()
for e in range(100):
    sida = r1.predict(data)
    bo.salvar(r1,e)
    r1 = bo.load("Elite-epoca-"+str(e));
    sida2 = r1.predict(data)
    if(sida== sida2):
        print("foi")
    else:
        print("não foi")
