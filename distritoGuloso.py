
"""
    Warning
        TA TD ERRADO NESSA merda
        PQ CADA FUNÇÂO TÀ TRATANDO O CENTRO DO SISTEMA COMO ALGO DIFERENTE

        A FUNÇÂO QUE RETORNA OS SEEDS ESTÀ CORRETA!!!!

        DÀ pra manter se vc mudar a função que calcula a criminalidade, para aceitar
        um centro cartesiano que n seja 0,0 e sim x/2,y/2

        o mesmo para a função que determina os  seeds
"""

"""
    CENTRO CARTESIANO AGR EH x/2,y/2

"""

from copy import deepcopy
from random import randint
import math
from cidadeAleatoria import geraCidadeAleatoria
from statistics import pstdev
from collections import namedtuple

def achaPontosCirculo(raio, numPontos):
    """
        Warning, essa merda gera numero negativo

        Mas agr vc qrr ponto negativo, viva o coupling!
    """
    Ponto = namedtuple('Ponto', ['x','y'])
    pontos = []
    for i in range(numPontos):
        x = int(raio * math.cos(2 * math.pi * i / numPontos))
        y = int(raio * math.sin(2 * math.pi * i / numPontos))
        ponto = Ponto(x,y)
        pontos.append(ponto)

    return pontos

def determinaPosicoesSeeds(
        numSeeds, numCirculos, raioCirculoMenor, proporcaoCirculos, tamanhoXY):

    pontosPorCirculo = int(numSeeds / numCirculos)
    pontos = []
    raio = raioCirculoMenor
    
    for i in range(numCirculos):
        #pontos.append(achaPontosCirculo(raio, pontosPorCirculo))
        pontos += achaPontosCirculo(raio, pontosPorCirculo)
        raio *= proporcaoCirculos
    
    Ponto = namedtuple('Ponto', ['x','y'])
    return [Ponto(int(ponto.x + tamanhoXY.x/2), int(ponto.y + tamanhoXY.y/2))
            for ponto in pontos]

def achaSeeds(atomos, posicoesSeeds):
    """
        Dá treta aqui pq são namedtuples no posicoesSeeds
        essa merda pode ser inclusive um objeto...
    """
    seeds = [ a for a in atomos if 
            any(p.x == a.posicao.x and p.y == a.posicao.y 
            for p in posicoesSeeds)]
    
    return seeds

def somaViolenciaCluster(cluster):
    violencia = 0
    for atomo in cluster.elementos:
        violencia += atomo.qtdCrimes
    return violencia

def retIndClusterComVizMenosViolento(clusters):
    clusterMenosViolento = clusters[0]
    qtdCrimesClusterMV = somaViolenciaCluster(clusters[0]) 
    
    i = 0; indiceMenosViolento = 0
    for cluster in clusters:
        violenciaCluster =  somaViolenciaCluster(cluster)
        if violenciaCluster < qtdCrimesClusterMV and len(cluster.vizinhos) > 0:
            clusterMenosViolento = cluster 
            qtdCrimesClusterMV = violenciaCluster
            indiceMenosViolento = i
        i+=1
    return indiceMenosViolento

def retornaVizinhosAtualizado(cluster, novoAtomoAdicionado):
    vizinhancaAnterior = [ vizinho for vizinho in cluster.vizinhos 
            if not vizinho is novoAtomoAdicionado ]
    vizinhosNovos = [ x for x in novoAtomoAdicionado.vizinhos
            if x not in vizinhancaAnterior ]
    return vizinhancaAnterior + vizinhosNovos 

def clusterizaGuloso(seeds):
    Cluster = namedtuple('Cluster', ['elementos', 'vizinhos'])
    clusters = [Cluster([seed],seed.vizinhos) for seed in seeds]

    clustersComVizinhos = [ x for x in clusters if len(x.vizinhos) > 0 ]
    while len(clustersComVizinhos) > 0:
        i = retIndClusterComVizMenosViolento(clusters)
        novoAtomoAdicionado = clusters[i].vizinhos[0]
        clusters[i].elementos.append(novoAtomoAdicionado)
        clusters[i] = Cluster(clusters[i].elementos,
                retornaVizinhosAtualizado(clusters[i], novoAtomoAdicionado)) 

        # retira o novoAtomoAdicionado dos vizinhos dos outros clusters
        clusters = [ Cluster(x.elementos, [ v for v in x.vizinhos 
                if not (v is novoAtomoAdicionado) ]) for x in clusters  ]
        
        clustersComVizinhos = [ x for x in clusters if len(x.vizinhos) > 0 ]
    
    return clusters


def clusterizaAleatorio(seeds):
    Cluster = namedtuple('Cluster', ['elementos', 'vizinhos'])
    clusters = [Cluster([seed],seed.vizinhos) for seed in seeds]

    clustersComVizinhos = [ x for x in clusters if len(x.vizinhos) > 0 ]
    while len(clustersComVizinhos) > 0:
        i = randint(0, len(seeds) - 1)
        while not len(clusters[i].vizinhos) > 0 :
            i = randint(0, len(seeds) - 1)
        novoAtomoAdicionado = clusters[i].vizinhos[0]
        clusters[i].elementos.append(novoAtomoAdicionado)
        clusters[i] = Cluster(clusters[i].elementos,
                retornaVizinhosAtualizado(clusters[i], novoAtomoAdicionado)) 

        clusters = [ Cluster(x.elementos, [ v for v in x.vizinhos 
                if not (v is novoAtomoAdicionado) ]) for x in clusters  ]

        clustersComVizinhos = [ x for x in clusters if len(x.vizinhos) > 0 ]

    return clusters

Ponto = namedtuple('Ponto',['x','y'])
tamanhoXY = Ponto(25,25)

"""
    Vc tem que tratar o fato de que determinados circulos n passam por n seeds

    tem que tratar numero de seeds não divisivel pelo numero de circulos
"""
numCirculos = 2; raioCirculoMenor = 5; proporcaoCirculos = 2; numSeeds = 8; 
atomosGulosos = geraCidadeAleatoria(tamanhoXY)
posicoesSeeds = determinaPosicoesSeeds(
        numSeeds, numCirculos, raioCirculoMenor, proporcaoCirculos, tamanhoXY)

seedsGulosos = achaSeeds(atomosGulosos, posicoesSeeds)
print("Desvio padrão qtdCrimes Clusterização Gulosa")

print([sum([x.qtdCrimes for x in cluster.elementos]) 
        for cluster in clusterizaGuloso(seedsGulosos)])

print(pstdev([sum([x.qtdCrimes for x in cluster.elementos]) 
        for cluster in clusterizaGuloso(seedsGulosos)]))

atomosAleatorios = deepcopy(atomosGulosos)
seedsAleatorios = achaSeeds(atomosAleatorios, posicoesSeeds)
print("Desvio padrão CLusterização Aleatória")

print([sum([x.qtdCrimes for x in cluster.elementos]) 
        for cluster in clusterizaAleatorio(seedsAleatorios)])

print(pstdev([sum([x.qtdCrimes for x in cluster.elementos]) 
        for cluster in clusterizaAleatorio(seedsAleatorios)]))
