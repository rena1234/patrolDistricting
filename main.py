from distritoGuloso import distrita_guloso
from trab_final import sim_annealing
from collections import namedtuple

Atomo_SA = namedtuple('Atomo_SA', 
        ['qtd_crimes', 'posicoes_vizinhos','num_cluster']
)

Cluster_SA = namedtuple('Cluster', ['posicoes_atomos', 'criminalidade'])

Ambiente = namedtuple('Ambiente', ['clusters','matriz_atomos'])

Ponto = namedtuple('Ponto',['x','y'])
tamanhoXY = Ponto(25,25)

matriz_atomos = [ 
        [None for i in range(tamanhoXY.x)] for j in range(tamanhoXY.y)
]

Opcoes = namedtuple(
        'Opcoes', ['n', 't_inicial', 't_final', 'a', 'compact_tax']
)

clusters = distrita_guloso()

clusters_sa = []
for i,cluster in enumerate(clusters):
    qtd_crimes = 0; posicoes_atomos = []
    for atomo in cluster.elementos:
        posicoes_atomos.append(atomo.posicao)
        qtd_crimes += atomo.qtdCrimes
        posicoes_vizinhos = [ 
                Ponto(v.posicao.x, v.posicao.y) for v in atomo.vizinhos 
        ] 
        matriz_atomos[atomo.posicao.x][atomo.posicao.y] = Atomo_SA(
                atomo.qtdCrimes, posicoes_vizinhos, i
        )
    clusters_sa.append(Cluster_SA(posicoes_atomos, qtd_crimes))

ambiente = Ambiente(clusters_sa, matriz_atomos)
Opcoes = namedtuple(
        'Opcoes', ['taxa_dec', 't_inicial', 't_final'
            ,'num_itr_temp', 'compact_tax']
)
opcoes = Opcoes(0.6, 10, 0.1, 100, 222) 

print("Desvio padrão SA:")
print(sim_annealing(ambiente, opcoes))
