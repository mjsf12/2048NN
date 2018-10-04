from mxnetNN import Rede
from mxnet import nd, autograd, gluon
from BO import BO
from time import sleep
bo =BO()
data = nd.ones((1,16))
r1 = Rede()
r2 = Rede()
for _ in range(1):
    print ("pai:")
    print(r1.get_genes())
    print ("mae:")
    print(r2.get_genes())
    filho=bo.filhos(r1,r2)
    print ("filho")
    print (filho.get_genes())
    