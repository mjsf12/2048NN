from mxnetNN import Rede
from mxnet import nd, autograd, gluon
from BO import BO
from time import sleep
bo =BO()
data = nd.ones((1,16))
r1 = Rede()
r2 = Rede()
sleep(1)
while True:
    print(bo.filhos(r1,r2))
    