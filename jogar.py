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
        self.pontos = (np.sum(self.tabuleiro) + np.amax(self.tabuleiro)*10)

    def Print(self):
        print(self.tabuleiro)

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
            os.system('clear')    
            if not 0 in self.tabuleiro or 11 in self.tabuleiro:
                break
            self.Colocar_Aleatrio()
            self.Print()
            tecla = self.Teclado()
            print(tecla)
            self.Calcular_novo_tabuleiro(tecla)
            self.rodadas += 1
            sleep(i)
        self.Pontos()

bo = BO()
nn=bo.load("Elite-epoca-5")
game = Game(4,nn)
game.LoopGame(0.5)
