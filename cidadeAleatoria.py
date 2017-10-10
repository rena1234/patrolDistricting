"""
    Warning
        TA TD ERRADO NESSA merda
        PQ CADA FUNÇÂO TÀ TRATANDO O CENTRO DO SISTEMA COMO ALGO DIFERENTE

        
"""
import math
from random import randint
from collections import namedtuple

def distanciaDoisPontos(ponto1, ponto2):
    return math.sqrt(pow(ponto1.x - ponto2.x) + pow(ponto1.y - ponto2.y))

def achaVizinhos(atomo, atomos, tamanhoXY):
    vizinhos = []
    for x in range(atomo.posicao.x - 1, atomo.posicao.x + 2):
        for y in range(atomo.posicao.y - 1, atomo.posicao.y + 2):
            if ( x == atomo.posicao.x and y == atomo.posicao.y ):
                continue
            elif (0 <= x < tamanhoXY.x) and (0 <= y < tamanhoXY.y):
                vizinhos.append(atomos[tamanhoXY.x * x + y])
    return vizinhos        

def calculaCriminalidade(posicaoNovoAtomo, criminalidadeVizinhos, tamanhoXY):
    if len(criminalidadeVizinhos) > 1:
        return int(sum(criminalidadeVizinhos)/len(criminalidadeVizinhos))

    return int( 1/(abs(posicaoNovoAtomo.x - tamanhoXY.x) 
            + abs(posicaoNovoAtomo.y - tamanhoXY. y) + 1) * randint(100, 300))

def geraCidadeAleatoria(tamanhoXY):

    def achaVizinhosJaCriados(tamanhoXY, posicaoAtomo, atomos):

        if posicaoAtomo.x == 0 and posicaoAtomo.y == 0:
            return []

        if posicaoAtomo.y == 0:
            indiceBase = ((posicaoAtomo.x - 1 ) * tamanhoXY.x + 
                    posicaoAtomo.y)
            return [ a for a in atomos[indiceBase: indiceBase + 1]]
        
        if x == 0:
            return [ atomos[posicaoAtomo.x * tamanhoXY.x + posicaoAtomo.y -1]]            

        indiceBase = (posicaoAtomo.x - 1 ) * tamanhoXY.x + posicaoAtomo.y - 1
        vizinhosCima = [ a for a in atomos[indiceBase: indiceBase + 2]]
        return vizinhosCima + [
                atomos[posicaoAtomo.x * tamanhoXY.x + posicaoAtomo.y - 1] ]

    Atomo = namedtuple('Atomo', ['nome', 'posicao', 'qtdCrimes', 'vizinhos'])
    Ponto = namedtuple('Ponto', ['x','y'])

    atomos = []
    for x in range(tamanhoXY.x):
        for y in range(tamanhoXY.y):
            posicao = Ponto(x,y)
            qtdCrimes = calculaCriminalidade(posicao,[vizinho.qtdCrimes 
                    for vizinho 
                    in achaVizinhosJaCriados(tamanhoXY, posicao, atomos)],
                    tamanhoXY)
            atomos.append(Atomo('a', posicao, qtdCrimes, []))

    cidadeAleatoria = [ Atomo(atomo.nome, atomo.posicao, atomo.qtdCrimes, 
            achaVizinhos(atomo, atomos, tamanhoXY))
            for atomo in atomos ]
    
    
    return cidadeAleatoria
