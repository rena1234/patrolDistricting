from collections import namedtuple
import math

def achaPontosCirculo(raio, numPontos):
    """
            for(var i = 0; i < items; i++) {
            var x = x0 + r * Math.cos(2 * Math.PI * i / items);
            var y = y0 + r * Math.sin(2 * Math.PI * i / items);
            }
    """
    Ponto = namedtuple('Ponto', ['x','y'])
    pontos = []
    for i in range(numPontos):
        x = raio * math.cos(2 * math.pi * i / numPontos)
        y = raio * math.sin(2 * math.pi * i / numPontos)
        ponto = Ponto(x,y)
        pontos.append(ponto)

    return pontos
	

def carregaAtomos(arquivo):
    Atomo = namedtuple('Atomo', ['nome', 'posicao', 'qtdCrimes', 'vizinhos'])
    atomos = []
    return atomos

def determinaPosicoesSeeds(numSeeds, numCirculos, raioCirculoMenor, proporcaoCirculos):
    pontosPorCirculo = numSeeds / numCirculos
    pontos = []
    raio = raioCirculoMenor
    
    for i in range(numCirculos):
            pontos.append(achaPontosCirculo(raio, pontosPorCirculo))
            raio *= proporcaoCirculos
    
    return pontos

def achaSeeds(atomos, posicoesSeeds):
    seeds = [ x for x in atomos if (x.posicao.x , x.posicao.y) in posicoesSeeds ]

def distanciaDoisPontos(ponto1, ponto2):
    return sqrt(pow(ponto1.x - ponto2.x) + pow(ponto1.y - ponto2.y))

def selecionaAtomo(atomosNaoSelecionados, seed):

def criaDistritos(atomos, seeds):
    atomosNaoSelecionados = [ x for x in atomos if not x in seeds ]
    
    distritos = []

atomos = carregaAtomos()
raioCirculoMenor = 
distritos = criaDistritos(atomos,determinaSeeds(atomos, raioCirculoMenor))

