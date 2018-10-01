from BO import BO
from Tensor import Rede_neural
import pickle

bo = BO()
r1 = Rede_neural()
r2 = Rede_neural()
r1=r1.getWid()
r2=r2.getWid()

with open(r1, 'wb') as f:
    pickle.dump(r1, f)
with open(r2, 'wb') as f:
    pickle.dump(r2, f)

#print(bo.pegar_meio(r1.getWid(),r2.getWid()))
