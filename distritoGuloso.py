from copy import deepcopy
"""
def criaDistritos(atomos, seeds, numIters):

    def retornaUmVizinho(cluster):
        vizinho = None
        for atomo in cluster:
            #usar if ternario aqui
            if atomo.vizinhos not #vazio:
                vizinho  = atomo.vizinhos[0]
                break
        return vizinho

    def divClustersSameSize(seeds, atomos):
        clusters = [[]]

        #list comprehension for 2d array
        vizinhosClusters = [[] x for  ]
        atomosNaoSelecionados = [ x for x in atomos if not x in seeds ]
        
        #enquanto atomosNaoSelecionados for diferente de vazio
        while():
            for i in range(len(seeds)):
                novoAtomo = retornaUmVizinho(clusters[i])
                vizinhos[i].append(novoAtomo.vizinhos)

"""

def somaViolenciaCluster(cluster):
    violencia = 0
    for atomo in cluster.elementos:
        violencia += atomo.qtdCrimes()
    return violencia
"""
def retornaClusterMaisViolento(clusters):
    clusterMaisViolento = clusters[0]
    qtdCrimesClusterMV = somaViolenciaCluster(clusters[0]) 

    for cluster in clusters:
        violenciaCluster =  somaViolenciaCluster(cluster)
        if violenciaCluster > qtdCrimesClusterMV:
            clusterMaisViolento = cluster 
            qtdCrimesCluster = violenciaCluster

    return clusterMaisViolento
"""

def retornaClusterMenosViolento(clusters):

    clusterMenosViolento = clusters[0]
    qtdCrimesClusterMV = somaViolenciaCluster(clusters[0]) 

    for cluster in clusters:
        violenciaCluster =  somaViolenciaCluster(cluster)
        if violenciaCluster < qtdCrimesClusterMV:
            clusterMaisViolento = cluster 
            qtdCrimesClusterMV = violenciaCluster

    return clusterMaisViolento

def retornaNovosVizinhos(cluster, novoAtomoAdicionado):
    vizinhos = [ vizinho for vizinho in 

def clusterizacaoGulosa(seeds, desvioPadraoMin, maxIters):
    """
        treta aqui:
        maxIters tem que ser maior que o número de atomos
        e tem que fzr um procedimento extra ( ou mudar o atual )
        para os atomosque sobrarem, eles podem sobrar caso um cluster fique
        cercado, considerando esse algoritmo que vc planejava programar
    """

    Cluster = namedtuple('Cluster', ['elementos', 'vizinhos'])
    clusters = [Cluster([seed],seed.vizinhos) for seed on seeds]
    
    for i in range(maxIters):
        clusterMenosViolento = retornaClusterMenosViolento(clusters)
        clusterMenosViolento.elementos.append(clusterMenosViolento.vizinhos[0])
        clusterMenosViolento.vizinhos = 

        
"""
def divClustersSameSize(atomos, numClusters):

    def criaClusterVizinhos(atomoSeed, atomos, tamanhoCluster):
        atomosNaoSelecionados = [ atomo for atomo in atomos 
                and atomo not is atomoSeed ]
        cluster = []
        while len(cluster) < tamanhoCluster and len(atomosNaoSelecionados) > 0:

 """       


