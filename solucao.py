from collections import deque
from queue import PriorityQueue
import time

OBJETIVO_FINAL = "12345678_"

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
    nodos = []
    for acao in sucessores:
        nodos.append(Nodo(acao[1], nodo, acao[0], nodo.custo + 1))
    return nodos

def percurso_para_raiz(nodo):
    """
    Receberá um nó e retornará o percurso do nó até raiz
    """
    percurso = []
    nodo_atual = nodo

    while nodo_atual.pai:
        percurso.insert(0, nodo_atual.acao)
        nodo_atual = nodo_atual.pai

    return percurso


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    explorados = set()
    fronteira = deque([Nodo(estado, None, None, 0)])

    while True:
        if not fronteira:
            return None

        estado_corrente = fronteira.popleft()

        if estado_corrente.estado == OBJETIVO_FINAL:
            return percurso_para_raiz(estado_corrente)
        elif estado_corrente not in explorados:
            explorados.add(estado_corrente)
            for no_filho in expande(estado_corrente):
                fronteira.append(no_filho)


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
    explorados = set()
    fronteira = [Nodo(estado, None, None, 0)]

    while True:
        if not fronteira:
            return None

        estado_corrente = fronteira.pop()

        if estado_corrente.estado == OBJETIVO_FINAL:
            return percurso_para_raiz(estado_corrente)
        elif estado_corrente not in explorados:
            explorados.add(estado_corrente)
            for no_filho in expande(estado_corrente):
                fronteira.append(no_filho)

def h_hamming(estado):
    """
    A partir de um estado, calcula a distância de Hamming entre ele e o
    estado de objetivo final. Retorna a quantidade de peças que estão fora do lugar
    """
    return sum([1 for qnt1, qnt2 in zip(OBJETIVO_FINAL, estado) if qnt1 != qnt2])

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
    explorados = set()
    fronteira = []

    heappush(fronteira, (h_hamming(estado), Nodo(estado, pai=None, acao="", custo=0)))

    while True:
        if len(fronteira) == 0:
            return None
        estado_corrente = heappop(fronteira)
        if estado_corrente[1].estado == OBJETIVO_FINAL:
            return percurso_para_raiz(estado_corrente[1])
        if estado_corrente[1].estado not in explorados:
            explorados.add(estado_corrente[1].estado)
            for vizinho in expande(estado_corrente[1]):
                heappush(fronteira, (vizinho.custo + h_hamming(vizinho.estado), vizinho))


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
