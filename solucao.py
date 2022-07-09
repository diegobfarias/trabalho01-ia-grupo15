class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

def estado_para_array(estado):
    """
    Receberá um estado e retornará ele em formato de matriz, 
    que é um array de array
    """
    numeros = [char for char in estado]
    return [numeros[i : i + 3] for i in range(o, len(numeros), 3)]

def estado_para_string(estado):
    """
    Receberá um estado, em formato de matriz, e retornará
    em formato de string
    """
    return "".join([str(pos) for pos in sum(estado, [])])

def estado_movimento(estado, numero):
    """
    Recebe o estado em matriz, faz o deparser e substitui o vazio
    pelo número em questão
    """
    estado_string = estado_para_string(estado)
    return estado_string.replace(numero, "x").replace("_", numero).replace("x", "_")


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucessores = []
    y_vazio = 0
    x_vazio = 0
    estado = estado_para_array(estado)

    for i in range(3):
        for j in range(3):
            if estado[i][j] == "_":
                y_vazio = i
                x_vazio = j

    for i in range(3):
        for j in range(3):
            distancia_y = i - y_vazio
            distancia_x = j - x_vazio
            if estado[i][j] != "_" and (abs(distancia_y) + abs(distancia_x) == 1):
                sentido = ""
                if distancia_y == 1:
                    sentido = "abaixo"
                elif distancia_y == -1:
                    sentido = "acima"
                elif distancia_x == 1:
                    sentido = "direita"
                elif distancia_x == -1:
                    sentido = "esquerda"

                sucessores.append((sentido, estado_movimento(estado, estado[i][j])))
    return sucessores


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucessores = sucessor(nodo.estado)
    nodos = [Nodo(0,0,0,0) for i in sucessores]
    k=0

    for i in nodos:
        (nodos[k]).estado = sucessores[k][1]
        (nodos[k]).pai = nodo
        (nodos[k]).acao = sucessores[k][0]
        (nodos[k]).custo = (nodo.custo)+1
        k=k+1
        
    return nodos

def percurso(nodo):
    """
    Receberá um nó e retornará o percurso do nó inicial até o objetivo
    """
    acoes = []

    while nodo.pai is not None:
        acoes += [nodo.acao]
        nodo = nodo.pai

    return acoes[::-1]


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    primeiroNodo = Nodo(estado,None,None,0)
    explorados = []
    fronteira = [primeiroNodo]
    visitado = []
    while True:
        if fronteira == []:
            visitado = fronteira.pop(0)
            fronteira.pop(0)
        if visitado.estado == "12345678_":
            return "abaxate"
        if visitado.estado not in explorados
            explorados.append(v)
            vizinhos = expande(visitado)
            fronteira.extend(vizinhos)
            
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    fronteira = []
    visitados = set([])
    raiz = Nodo(estado, None, None, 0)
    k = raiz

    fronteira.append(raiz)

    while fronteira:
        k = fronteira.pop()
        if k.estado in visitados:
            continue
        if k.estado == OBJETIVO_FINAL:
            break
        fronteira.extend(expande(k))
        visitados.add(k.estado)

    if k.estado != OBJETIVO_FINAL:
        return None

    return percurso(k)


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    fronteira = []
    visitados = set()

    heappush(fronteira, ())


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
