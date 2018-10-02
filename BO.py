from Tensor import Rede_neural
import numpy as np
import os
from mxnetNN import Rede
class BO ():
    def __init__(self):
        pass
    def mutacao(self,neural):
        wid = neural.get_genes()
        aux  = wid
        while (True):
            num = np.random.randint(len(aux))-1
            shape=0
            try:
                shape = aux[num].shape
            except:
                pass
            if (shape==(1,)):
                aux[num][0] = np.random.uniform(-1,1)
                break
            aux = aux[num]
        neural.set_genes(wid)
        return neural

    def filhos(self,pai,mae):
        widP = pai.get_genes()
        widM = mae.get_genes()
        widF= self.pegar_meio(widP,widM)
        filho = Rede()
        filho.set_genes(widF)
        return filho
    
    def pegar_meio(self, widP,widM):
        num = np.random.randint(len(widP)) -1
        print(num)
        shape = 0
        try:
            shape = widP[num].shape
        except:
            pass
        if (shape==(1,)):
            return (np.concatenate((widP[:num],widP[num],widM[num+1:])))
        meio = self.pegar_meio(widP[num],widM[num])
        return np.concatenate((widP[:num],meio,widM[num+1:]))
        
    def Suruba(self,melhores):
        filhos = []
        z=0
        for x in melhores:
            for y in melhores:
                z = z+1
                print("reprodução:")
                print((z/(10*10))*100)
                if x[0] is y[0]:
                    os.system('clear')    
                    continue
                filho=self.filhos(x[0],y[0])
                if np.random.rand() < 0.1:
                    filho = self.mutacao(filho)
                filhos.append([filho,0])
                os.system('clear')     
        return melhores+filhos

    def recalcular(self,todos):
        antigos=[]
        for x in todos[:10]:
            antigos.append([x[0],0])
        antigos=self.Suruba(antigos)
        novos = []
        for _ in range(10):
            novos.append([Rede(),0])
        return antigos+novos
    
    def Criar_inicio(self):
        volta = []
        z=0
        for _ in range(110):
            z = z+1
            print("Criando Redes:")
            print((z/110)*100)
            volta.append([Rede(),0])
            os.system('clear') 
        return volta    




        
