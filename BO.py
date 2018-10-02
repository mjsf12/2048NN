from Tensor import Rede_neural
import numpy as np
import os
from mxnetNN import Rede
class BO ():
    def __init__(self):
        pass
    def mutacao(self,neural):
        wid = neural#.getWid()
        aux  = wid
        while (True):
            num = np.random.randint(len(aux))
            if (len(aux[num]==1)):#not hasattr(aux[num], "__len__")):
                aux[num][0] = np.random.uniform(-1,1)
                break
            aux = aux[num]
        #neural.setWid(wid)
        return neural

    def filhos(self,pai,mae):
        widP = pai.getWid()
        widM = mae.getWid()
        widF= self.pegar_meio(widP,widM)
        filho = Rede_neural(widF)
        return filho
    
    def pegar_meio(self, widP,widM):
        num = np.random.randint(len(widP))
        if (len(widP[num]==1)):
            return (widP[:num]+[widP[num]]+widM[num+1:])
        meio = self.pegar_meio(widP[num],widM[num])
        return widP[:num]+meio+widM[num+1:]
        
    def Suruba(self,melhores):
        filhos = []
        z=0
        for x in melhores:
            for y in melhores:
                z = z+1
                print("reprodução:")
                print((z/(110*110))*100)
                if x is y:
                    os.system('clear')    
                    continue
                filho=self.filhos(x,y)
                if np.random.rand() < 0.1:
                    filho = self.mutacao(filho)
                filhos.append(filho)
                os.system('clear')     
        return melhores+filhos

    def recalcular(self,todos):
        antigos=[]
        for x in todos[:10]:
            antigos.append(x[0])
        antigos=self.Suruba(antigos)
        novos = []
        for _ in range(10):
            novos.append([Rede_neural(),0])
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




        
