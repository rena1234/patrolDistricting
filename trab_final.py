from collections import namedtuple
from random import randint

Cluster = namedtuple('Cluster', ['elementos', 'criminalidade'])
Atomo = namedtuple('Atomo', ['nome', 'posicao', 'qtdCrimes', 'vizinhos'
        ,'num_cluster'])
Ponto = namedtuple('Ponto', ['x','y'])

def retorna_rand_viz_outro_cluster(num_cluster, vizinhos)

def verifica_compact_tax(clusters):
    return compact_tax

def gera_sol_vizinha(clusters, compact_tax):
    cl_perdedor = clusters[randint(0,len(clusters) -1)]

    
def sim_annealing(clusters, n, t_inicial, t_final, a, compact_tax):
    temp = t_inicial
    melhor = clusters
    while temp > t_final:

    return clusters_atualizados


