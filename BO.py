from Tensor import Rede_neural
import numpy as np
import os
from mxnetNN import Rede
from mxnet import nd
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
        num = np.random.randint(1,len(widP)+1) -1
        shape = 0
        try:
            shape = widP[num].shape
        except:
            pass
        if (shape==(1,)):
            aux = None           
            aux =np.append(widP[:num].asnumpy(),widP[num].asnumpy())
            try:
                aux = np.append(aux,widM[num+1:].asnumpy())
            except:
                pass
            aux.reshape(widP.shape)         
            aux = nd.array(aux)
            return aux
        meio = self.pegar_meio(widP[num],widM[num])
        aux = None
        try:
            aux =np.append(widP[:num].asnumpy(),meio.asnumpy())
            try:
                aux = np.append(aux,widM[num+1:].asnumpy())
            except:
                pass
            aux=aux.reshape(widP.shape)
            aux = nd.array(aux)

        except:
            try:
                aux =  [meio] +widM[num+1:]
            except:
                aux = [meio]
            aux =  widP[:num] +  aux
        return aux
        
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


    def Suruba_Votação( self,array):
        filhos = []
        for x in range(len(array)):
            if x == 0:
                continue
            else:
                array[x][1] = array[x-1][1] + array[x][1]
        for _ in range(100):
            pai = np.random.randint(array[-1][1])
            mae = np.random.randint(array[-1][1])
            pmae = False
            ppai = False
            for x in range(len(array)):
                if ppai and pmae:
                    break
                if not pmae:
                    if(array[x][1]>=mae):
                        mae = array[x-1]
                        pmae = True
                if not ppai: 
                    if(array[x][1]>=pai):
                        pai = array[x-1]
                        ppai = True
            fii = self.filhos(pai[0],mae[0])
            if (np.random.rand() <= 0.02):
                fii = self.mutacao(fii)
            filhos.append([fii,0])
        return(filhos)
        

    def recalcular(self,todos):
        return self.Suruba_Votação(todos)
    
    
    def recalcular_old(self,todos):
        antigos=[]
        for x in todos[:10]:
            antigos.append([x[0],0])
        antigos=self.Suruba(antigos)
        novos = []
        for _ in range(10):
            novos.append([Rede(),0])
        return antigos+novos

    def salvar(self, elite, epoca):
        elite.save_parameters("elites/Elite-epoca-"+str(epoca))
        
    def load(self,name):
        re  = Rede()
        re.load_parameters("elites/"+name)
        return re


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




        
