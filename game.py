import numpy as np
from time import sleep
from Tensor import Rede_neural
from BO import BO
import os
class Game():
    def __init__(self, tmn,RN):
        self.tmn = tmn
        self.CriarTabuleiro()
        self.RN = RN

    def CriarTabuleiro(self):
        self.tabuleiro = np.zeros((self.tmn,self.tmn))
        self.pontos = 0
        self.rodadas = 0
        self.Colocar_Aleatrio()

    def Colocar_Aleatrio(self):
        while True:
            i = np.random.randint(0,self.tmn)
            j = np.random.randint(0,self.tmn)
            if self.tabuleiro[i][j] == 0:
                self.tabuleiro[i][j] = 1
                break

    def Pontos(self):
        self.pontos = (np.sum(self.tabuleiro) + np.max(self.tabuleiro)*4)

    def Print(self):
        print(self.tabuleiro)
        print(self.pontos)

    def Teclado(self):
        aux=self.RN.predict(self.tabuleiro)
        if aux == 0 :
            return 'c'
        elif aux == 1:
            return 'b'
        elif aux == 2:
            return 'e'
        else :
            return 'd'
       

    def esqdit(self,tabu):
        novo_tabuleiro = []
        for linha in tabu:
            l = []
            mem = []
            zeros = []
            for item in linha:
                if not item == 0:
                    mem.append(item)
                else:
                    zeros.append(0)
            aux = 0
            aux2 = []
            for item in mem:
                if aux == 0:
                    aux = item
                else:
                    if aux == item:
                        zeros.append(0)
                        aux += 1
                    else:
                        aux2.append(aux)
                        aux = item
            if not aux == 0:
                aux2.append(aux)
            l = zeros + aux2
            novo_tabuleiro.append(l)      
        self.tabuleiro = np.array(novo_tabuleiro)

    def diresq(self,tabu):
        novo_tabuleiro = []
        for linha in tabu:
            l = []
            mem = []
            zeros = []
            for item in reversed(linha):
                if not item == 0:
                    mem.insert(0,item)
                else:
                    zeros.append(0)
            aux = 0
            aux2 = []
            for item in reversed(mem):
                if aux == 0:
                    aux = item
                else:
                    if aux == item:
                        zeros.insert(0,0)
                        aux += 1
                    else:
                        aux2.insert(0,aux)
                        aux = item
            if not aux == 0:
                aux2.insert(0,aux)
            l = aux2 +zeros
            novo_tabuleiro.append(l)      
        self.tabuleiro = np.array(novo_tabuleiro)

    def cimabaixo(self, tabu):
        self.esqdit(tabu.transpose())
        self.tabuleiro = self.tabuleiro.transpose()

    def baixocima(self, tabu):
        self.diresq(tabu.transpose())
        self.tabuleiro = self.tabuleiro.transpose()           

    def Calcular_novo_tabuleiro(self,tecla):
        if (tecla == 'c'):
            self.baixocima(self.tabuleiro)
        elif (tecla == 'b'):
            self.cimabaixo(self.tabuleiro)
        elif (tecla == 'e'):
            self.diresq(self.tabuleiro)
        else:
            self.esqdit(self.tabuleiro)

    def LoopGame(self,i):
        while True:
            if not 0 in self.tabuleiro or 11 in self.tabuleiro:
                break
            self.Colocar_Aleatrio()
            tecla = self.Teclado()
            self.Calcular_novo_tabuleiro(tecla)
            self.rodadas += 1
            sleep(i)
        self.Pontos()

po = []
def sunss(num):
    return num[1]

def me (array):
    todos = 0
    for x in array:
        aux=sunss(x)
        todos = aux + todos
    return todos/len(array)
epocas = 100
bo = BO()
array = bo.Criar_inicio()
melhor=0
tabu=[]
Elite = [0,0,0]
z=0
meme = 0
while True:
    if z ==51:
        break
    y=0
    z = z+1
    for x in array:
        y = y+ 1
        print("epoca")
        print(z)
        print ("Porcentagem do array")
        print ((y/110)*100)
        print ("Rodada anterior")
        print ("Melhor Resultado")
        print (melhor)
        print ("Tabuleiro")
        print (tabu)
        print ("ELITE")
        print ("Melhor Resultado")
        print (Elite[1])
        print ("Tabuleiro")
        print (Elite[2])
        print ("media anterior")
        print (meme)
        game = Game(4,x[0])
        game.LoopGame(0)
        x[1] = game.pontos
        x.append(game.tabuleiro)
        os.system('clear')        
    array = sorted(array,key=sunss,reverse=True)
    melhor = array[0][1]
    tabu =array[0][2]
    meme = me(array) 
    if Elite[1] < melhor:
        Elite=array[0]
        bo.salvar(Elite[0],z)
    array = bo.recalcular(array)
    array.append([Elite[0],0])

