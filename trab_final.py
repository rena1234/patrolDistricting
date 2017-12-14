from statistics import pstdev
from collections import namedtuple
from random import randint
from copy import deepcopy
from operator import gt
from operator import lt
import math

Cluster = namedtuple('Cluster', ['posicoes_atomos', 'criminalidade'])
Atomo = namedtuple('Atomo', ['qtd_crimes', 'posicoes_vizinhos','num_cluster'])
Ponto = namedtuple('Ponto', ['x','y'])
Ambiente = namedtuple('Ambiente', ['clusters','matriz_atomos'])
Parametros = namedtuple(
        'Parametros', ['n', 't_inicial', 't_final', 'a', 'compact_tax']
)

def retorna_pos_atm_fronteira(cluster, num_cluster,  matriz_atomos):

    atms_ja_visitados = []
    while(True):
        pos_atm = cluster.posicoes_atomos[randint(0,len(cluster.atomos))]
        atm = matriz_atomos[pos_atm.x][pos_atm.y]
        """
        vizs_outro_cluster = [pos in atm.posicoes_vizinhos 
                if not(matriz_atomos[pos.x][pos.y].num_cluster == num_cluster)
        ]
        """
        vizs_outro_cluster = []
        for pos in atm.posicoes_vizinhos:
            if not (matriz_atomos[pos.x][pos.y].num_cluster == num_cluster):
                vizs_outro_cluster.append(pos_atm)

        if(len(vizs_outro_cluster)):
            return pos_atm

        atms_ja_visitados.append(atm)

def retorna_ind_cluster_viz(atm_front, matriz_atomos):
    atms_visitadas = []
    while(True):
        posicao_vizinho = atm_front.posicoes_vizinhos[
                randint(0,len(atm_front.posicoes_vizinhos) -1)
        ]
        atm = matriz_atomos[posicao_vizinho.x][posicao_vizinho.y]
        if not atm in atms_visitados and atm.num_cluster != atm_front.num_cluster:
            return atm.num_cluster	

def retorna_cluster_dominante(clusters, funcao_comparacao):
    dominante = clusterd[0]
    for cluster in clusters:
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
   return (len(retorna_cluster_dominante(clusters, gt))
            /len(retorna_cluster_dominante(clusters, lt))
   )



def retorna_mudanca(clusters, matriz_atomos):

    InfoMudanca = namedtuple('InfoMudanca',
            ['pos_atm_mudante', 'ind_cl_perdedor'
            , 'ind_cl_recipiente'])

    ind_cl_perdedor = randint(0,len(clusters) -1)
    pos_atm_mudante = retorna_pos_atm_fronteira(
            ambiente.clusters[ind_cl_perdedor], ind_cl_perdedor, matriz_atomos
    )
    atm_mudante = matriz_atomos[pos_atm_mudante.x][pos_atm_mudante.y]
    ind_cl_recipiente = retorna_ind_cluster_viz(atm_mudante)
    return InfoMudanca(atm_mudante, ind_cl_perdedor, ind_cl_recipiente)

def retorna_atm_atualizado(atm_mudante, ind_cl_recipiente):
    return Atomo(
            atm_mudante.qtd_crimes, atm_mudante.posicoes_vizinhos
            , ind_cl_recipiente
    )

def retorna_matriz_atualizada(matriz_atomos, p_atm, ind_cl_recipiente):
    matriz_atualizada = deepcopy(ambiente.matriz_atomos)
    matriz_atualizada[p_atm.x][p_atm.y] =  retorna_atm_atualizado(
        atm_mudante, ind_cl_recipiente
    )
    return matriz_atualizada

def retorna_cluster_sem_atm(cluster, pos_atm, criminalidade_atm):
    pos_atms = [p for p in cluster.posicoes_atomos
                if (p.x != pos_atm_mudante.x and p.y != pos_atm_mudante.y )]
    return Cluster(pos_atms, cluster.criminalidade - criminalidade_atm )

def retorna_clusters_atualizados(clusters, mudanca, matriz_atomos):
    clusters_atualizados = []
    pos_atm_mudante = mudanca.pos_atm_mudante
    for i,cluster in enumerate(clusters):
        cluster_atualizado = None
        if i == mudanca.ind_cl_perdedor:
            crim_atm = matriz_atomos[pos_atm_mudante].criminalidade
            clusters_atualizados.append(
                retorna_cluster_sem_atm(cluster, pos_atm_mudante, crim_atm)
            )
            
        else:
            clusters_atualizados.append(deepcopy(cluster))
    
    clusters_atualizados[mudanca.ind_cl_recipiente].posicoes_atomos.append(
            mudanca.pos_atm_mudante)

    return clusters_atualizados

def retorna_ambiente_atualizado(mudanca, ambiente):
    clusters_anterior = ambiente.clusters; matriz_anterior = ambiente.matriz_atomos
    pos_atm = mudanca.pos_atm_mudante, ind_recipiente = mudanca.ind_cl_recipiente
    clusters = retorna_clusters_atualizados(
            clusters_anterior, mudanca, matriz_anterior
    )
    matriz_atomos = retorna_matriz_atualizada(
            matriz_anterior, pos_atm_mudante, ind_recipiente
    )
    ambiente_atualizado = Ambiente(clusters, matriz_atomos)
    return ambiente_atualizado 

def gera_sol_vizinha(ambiente, compact_tax):
    clusters = ambiente.clusters; matriz_atomos = ambiente.matriz_atomos
    mudanca = retorna_mudanca(clusters, matriz_atomos)
    return retorna_ambiente_atualizado(mudanca, ambiente)

def retorna_sucesso(prob):
    sorteado = randint(1,100)
    sorteado = sorteado / 100
    if sorteado < prob:
        return True
    return False

def sim_annealing(solucao_inicial, opcoes):
    temp = opcoes.t_inicial; num_itr_temp = opcoes.num_itr_temp
    clusters = solucao_inicial.clusters
    melhor_sol = solucao_inicial
    stdev_melhor = pstdev([c.criminalidade for c in clusters])
    while temp > t_final:
        for i in range(num_itr_tempe):
            nova_sol =  gera_sol_vizinha(melhor_sol, opcoes.compact_tax)
            stdev_candidato = pstdev([c.criminalidade for c in clusters])
            """
                Ordem invertida em relação ao slide pois aqui, qnt maior
                o desvio padrao, pior
            """
            delta_e = stdev_melhor - stdev_candidato 
            if delta_e >= 0:
                melhor_sol = nova_sol
            elif retorna_sucesso(math.exp(-delta_e/temp)):
                melhor_sol = nova_sol
        temp = temp * opcoes.taxa_dec


    return clusters_atualizados

