from collections import namedtuple
from random import randint

Cluster = namedtuple('Cluster', ['atomos', 'criminalidade', 'num_cluster'])
Atomo = namedtuple('Atomo', ['nome', 'posicao', 'qtdCrimes', 'vizinhos'
        ,'num_cluster'])
Ponto = namedtuple('Ponto', ['x','y'])

def retorna_atm_fronteira(cluster):
	atms_ja_visitados = []
	while(True):
		atm = cluster.atomos[randint(0,len(cluster.atomos))]
		if(len([a in atm.vizinhos if a.num_cluster != cluster.num_cluster ])):
			return atm

def retorna_viz_outro_cluster(atm_front):
	atms_ja_visitados = []
	while(True)
		atm = atm_front_.vizinhos[randint(0,len(atm_front.vizinhos) -1)]
		if not atm in atms_ja_visitados and atm.num_cluster != atm_front.num_cluster:
			return atm	
		atms_ja_visitados = atm

	
def retorna_ind_mais_violento(clusters):
		indice = 0
		for i,cluster in enumerate(clusters):
			if cluster.criminalidade > clusters[indice].criminalidade:
				indice = i;
	    return indice

	def retorna_ind_menos_violento(clusters):
		indice = 0
		for i,cluster in enumerate(clusters):
			if cluster.criminalidade < clusters[indice].criminalidade:
				indice = i;
	    return indice

def retorna_compact_tax(clusters):
	
"""
	retornar proporcao entre areas e n~ao violencias
"""
	menor_violencia = clusters[retorna_ind_menos_violento(clusters)].criminalidade
    maior_violencia = clusters[retorna_ind_mais_violento(clusters)].criminalidade
    return maior_violencia / menor_violencia;

def gera_sol_vizinha(clusters, compact_tax):
    compact_tax = 
    cl_perdedor = clusters[randint(0,len(clusters) -1)]
    atm_mudante = 

    
def sim_annealing(clusters, n, t_inicial, t_final, a, compact_tax):
    temp = t_inicial
    melhor = clusters
    while temp > t_final:

    return clusters_atualizados
