
Atomo_SA = namedtuple('Atomo_SA', 
        ['qtd_crimes', 'posicoes_vizinhos','num_cluster']
)

Cluster_SA = namedtuple('Cluster', ['posicoes_atomos', 'criminalidade'])

matriz_atomos = [ 
        [None for i in range(tamanhoXY.x)] for j in range(tamanhoXY.y)
]

"""
for atomo in atomos:
    pos = atomo.posicao
    posicoes_vizinhos = [ 
            Ponto(v.posicao.x, v.posicao.y) for v in atomo.vizinhos 
    ] 
    matriz_atomos[pos.x][pos.y] = Atomo_SA(
            atomo.qtdCrimes, posicoes_vizinhos, 

"""
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
    clusters_sa.append(Cluster_SA(posicoes_atomos, qtd_crimes)
