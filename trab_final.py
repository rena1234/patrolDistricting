from collections import namedtuple
from random import randint
from copy import deepcopy
from operator import gt
from operator import lt

Cluster = namedtuple('Cluster', ['posicoes_atomos', 'criminalidade'])
Atomo = namedtuple('Atomo', ['qtdCrimes', 'posicoes_vizinhos','num_cluster'])
Ponto = namedtuple('Ponto', ['x','y'])
Ambiente = namedtuple('Ambiente', ['clusters','matriz_atomos'])

def retorna_atm_fronteira(cluster, num_cluster,  matriz_atomos):
    atms_ja_visitados = []
    while(True):
        atm = matriz_atomos[
                cluster.posicoes_atomos[randint(0,len(cluster.atomos))]
        ]
        if(len([a in atm.posicoes_vizinhos if not (a.num_cluster == num_cluster)])):
            return atm

def retorna_ind_cluster_viz(atm_front, matriz_atomos):
    atms_visitadas = []
    while(True)
        posicao_vizinho = atm_front.posicoes_vizinhos[
                randint(0,len(atm_front.posicoes_vizinhos) -1)
        ]
        atm = matriz_atomos[posicao_vizinho.x][posicao_vizinho.y]
        if not atm in atms_visitados and atm.num_cluster != atm_front.num_cluster:
            return atm.num_cluster	

def retorna_cluster_dominante(clusters, funcao_comparacao):
    dominante = clusterd[0]
    for cluster clusters:
        if funcao_comparacao(len(cluster.posicoes_atomos)
                ,len(dominante.posicoes_atomos)):
            dominante = cluster
    return dominante

"""
def retorna_tam_maior_cluster(clusters):
    tamanho = len(clusters[0].posicoes_atomos)
    for cluster in clusters:
    for i,cluster in enumerate(clusters):
        if len(cluster.matriz_atomos) > len(clusters[indice].matriz_atomos):
            indice = i;
    return indice

def retorna_tam_menor_cluster(clusters):
    tamanho = len(clusters[0].posicoes_atomos)
    for cluster in clusters:
        if len(cluster.matriz_atomos) < len(clusters[indice].matriz_atomos):
            indice = i;
    return indice

def retorna_compact_tax(clusters):
    tam_menor = len(clusters[retorna_ind_menor_cluster(clusters)]
    tam_maior = clusters[retorna_ind_maior_cluster(clusters)]
    return tam_maior / tam_menor;

"""

def retorna_compact_tax(clusters):
    return len(retorna_cluster_dominante(clusters, gt))
            /len(retorna_cluster_dominante(clusters, lt))



def gera_sol_vizinha(ambiente, compact_tax):
    InfoMudanca = namedtuple('InfoMudanca',['atm_mudante', 'ind_cl_perdedor'
            , 'ind_cl_recipiente'])
    
    def retorna_mudanca(clusters):
        ind_cl_perdedor = randint(0,len(clusters) -1)
        atm_mudante = retorna_atm_fronteira(ambiente.clusters[ind_cl_perdedor]) 
        ind_cl_recipiente = retorna_ind_cluster_viz(atm_mudante)
        return InfoMudanca(atm_mudante, ind_cl_perdedor, ind_cl_recipiente)


    def retorna_ambiente_atualizado(mudanca, ambiente):
        matriz_atualizada = deepcopy(ambiente.matriz_atomos)
        atm_mudante = mudanca.atm_mudante
        p_atm = atm_mudante.posicao
        matriz_atualizada[p_atm.x][p_atm.y] = Atomo(

        return ambiente_atualizado 
    def retorna_lista_pos_atm_lista

    mudanca = retorna_mudanca(clusters)
    recipiente = ambiente_atualizado.clusters[mudanca.ind_cl_recipiente]
    recipiente.posicoes_atomos.append(p_atm)
    recipiente.criminalidade += mudanca.atm_mudante.criminalidade
    perdedor = ambiente_atualizado.clusters[mudanca.ind_cl_perdedor]
    perdedor.criminalidade -= mudanca.atm_mudante.criminalidade
    

    return ambiente_atualizado


    
def sim_annealing(clusters, n, t_inicial, t_final, a, compact_tax):
    temp = t_inicial
    melhor = clusters
    while temp > t_final:

    return clusters_atualizados
