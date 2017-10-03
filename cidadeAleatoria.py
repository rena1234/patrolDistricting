import math
from random import randint

def distanciaDoisPontos(ponto1, ponto2):
    return math.sqrt(pow(ponto1.x - ponto2.x) + pow(ponto1.y - ponto2.y))

def calculaCriminalidade(atomo, atomosCrimCalculada):
    vizCrimCalculada = [ x for x in atomo.vizinhos and x in atomosCrimCalculada ]
    if len(vizCrimCalculada > 1):
        acmCrimesViz = 0
        for vizinho in vizCrimCalculada:
            acmCrimesViz += vizinho.qtdCrimes
        return acmCrimesViz/len(vizCrimCalculada)

    else:
        return ( 1/sqrt(pow(atomo.posicao.x) + pow(atomo.posicao.y)) 
                * randint(100, 300))

def achaVizinhos(atomo, atomos, tamanhoXY):
    vizinhos = []
    for x in range(atomo.posicao.x - 1, atomo.posicao.x + 2):
        for y in range(atomo.posicao.y - 1, atomo.posicao.y + 2):
            if ( x == y ):
                continue
            elif (0 <= x < tamanhoXY.x) and (0 <= y < tamanhoXY.y):
                vizinhos.append(atomos[tamanhoXY.x * x + y])

    return vizinhos        
    

def geraCidadeAleatoria(tamanhoXY, calculaCriminalidade):
    Atomo = namedtuple('Atomo', ['nome', 'posicao', 'qtdCrimes', 'vizinhos'])
    atomos = [ Atomo(posicao = (x,y)) for x in range(tamanhoXY.x) 
            for y in range(tamanhoXY.sty) ]
    
    atomosVizinhosCalculados = [ Atomo(posicao = atomo.posicao,
            vizinhos = achaVizinhos(atomo, atomos, tamanhoXY)) 
            for atomo in atomos ]

    atomosCrimCalculada = []
    for atomo in  atomosVizinhosCalculados:
        atomo.qtdCrimes = calculaCriminalidade(atomo, atomosCrimCalculada)
        atomosCrimCalculada.append(atomo)
    
    return atomosCrimCalculada
