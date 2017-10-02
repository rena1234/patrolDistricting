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


