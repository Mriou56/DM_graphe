import time

from Graph_List import *
from collections import defaultdict


### Class UnionFind ###
class UnionFind:
    def __init__(self):
        self.parents = {}

    def make_set(self, v):
        """
        :param v: a vertex
        :return: None
        """
        self.parents[v] = None

    def find(self, v):
        """
        :param v: a vertex
        :return: The root of the vertex
        """
        if self.parents[v] == None:
            return v
        else:
            return self.find(self.parents[v])

    def union(self, v1, v2):
        """
        :param v1: a vertex
        :param v2: a vertex
        :return: None
        """
        v1_root = self.find(v1)
        v2_root = self.find(v2)
        if v1_root != v2_root:
            self.parents[v1_root] = v2_root


### Sorting function ######

def BFS(graph, vertex: Vertex):
    """
    :param graph: the graph we study
    :param vertex: the vertex we begin with
    :return: [0] The path with the BFS way and [1] the dictionary of the first predecessors
    """
    queue = []
    grey = [vertex]
    pred = {v: None for v in graph.vertex()}
    parcours = []
    queue.append(vertex)
    while len(queue) != 0:
        val = queue.pop(0)  # To delete the first of the list
        parcours.append(val)
        succ = graph.succ(val)
        for i in succ:
            if i not in grey:
                pred[i] = val
                queue.append(i)
                grey.append(i)

    return parcours, pred


def DFSrec(graph, vertex=None):
    """
    :param graph: the graph we study
    :param vertex: the vertex we begin with
    :return: The path of the graph in a recursive way
    """
    color = {v: "white" for v in graph.vertex()}
    pred = {v: None for v in graph.vertex()}
    parcours = []

    def DFSinner(ver):
        color[ver] = "grey"
        for t in graph.succ(ver):
            if color[t] == "white":
                pred[t] = ver
                DFSinner(t)
        color[ver] = "black"
        parcours.append(ver)

    if vertex is not None:
        DFSinner(vertex)
    else:
        for v in graph.vertex():
            if color[v] == "white":
                DFSinner(v)

    return parcours


def DFStopo(graph, vertex=None):
    """
    :param graph: the graph we study
    :param vertex: the vertex we begin with
    :return: The path of the graph in a topologic way
    """
    color = {v: "white" for v in graph.vertex()}
    pred = {v: None for v in graph.vertex()}
    topo_order = []

    def DFSinner(ver):
        color[ver] = "grey"
        for t in graph.succ(ver):
            if color[t] == "white":
                pred[t] = ver
                DFSinner(t)
        color[ver] = "black"
        topo_order.insert(0, ver)

    if vertex is not None:
        DFSinner(vertex)
    else:
        for v in graph.vertex():
            if color[v] == "white":
                DFSinner(v)

    return topo_order


def is_connex(g):
    """
    :param g: the graph that we want to know his connexion
    """
    nbr_vertex = len(g.vertex())
    start = next(iter(g.vertex()))
    p_dfs = DFSrec(g, start)

    if nbr_vertex == len(p_dfs):
        print("Ce graphe est connexe.")
    else:
        print("Ce graphe n'est pas connexe.")


def connex_compo(graph):
    """
    :param graph: the graph we study
    :return: Lists of each connex compo
    """
    if not graph.directed:
        if is_connex(graph):
            return graph.BFS()
        else:
            color = {v: "white" for v in graph.vertex()}
            pred = {v: None for v in graph.vertex()}
            list_of_list = []
            parcours = []
            vertex = None

            def DFSinner(ver):
                color[ver] = "grey"
                for t in graph.succ(ver):
                    if color[t] == "white":
                        pred[t] = ver
                        DFSinner(t)
                color[ver] = "black"
                parcours.append(ver)

            if vertex is not None:
                DFSinner(vertex)
            else:
                for v in graph.vertex():
                    if color[v] == "white":
                        DFSinner(v)
                        list_of_list.append(parcours[:])
                        parcours.clear()
        return list_of_list
    else:
        print("Impossible pour un graphe orienté.")
        return False


def pcc(graph, vertex1, vertex2):
    """
    Find the shorter path between two vertex
    :param vertex1: the beginning vertex
    :param vertex2: the end vertex
    :param graph: the graph we study
    :return: The shorter path between two vertex
    """
    dic_pred = BFS(graph, vertex1)[1] # Complexity = nb edges + nb vertex
    pcc = []
    v = vertex2
    while dic_pred[v] is not None: # Complexity = nb edges + nb vertex
        pcc.append(v)
        v = dic_pred[v]
    pcc.append(v)
    pcc.reverse()
    return pcc  # Possible de faire list(reversed(pcc))


def kruskal_naive(graph):
    """
    :param graph: The graph we want to extract the arpm
    :return:
    """
    T = GraphList(False)
    liste_e = graph.edges()
    for v in graph.vertex():
        T.add_vertex(v)

    liste_e.sort(key=lambda x: (x[1][1]))
    for e in liste_e:
        T.add_edge(e[0], e[1][0], e[1][1])
        if T.cycled(e[0]):
            T.remove_edge(e[0], e[1][0], e[1][1])
    T.print()


def prim(graph, s):
    """
    :param graph: The graph we want to extract the arpm
    :return:
    """
    T = GraphList(False)
    liste_e = graph.edges()
    T.add_vertex(s)
    liste_e.sort(key=lambda x: (x[1][1]))
    min_e = None

    while len(T.vertex()) != len(graph.vertex()):
        min_w = 1000
        for u in list(T.vertex()):
            for v in graph.succ(u):
                if (u, v) in liste_e and u in T.vertex() and v[0] not in T.vertex():
                    # print(u, v)
                    if v[1] < min_w:
                        min_w = v[1]
                        min_e = (u, v[0])

        # print(min_e, min_w)
        T.add_vertex(min_e[1])
        T.add_edge(*min_e, min_w)
    T.print()


def kruskal_UF(graph):
    """
    :param graph: The graph we want to extract the arpm
    :return:
    """
    uf = UnionFind()
    T = GraphList(False)
    liste_e = graph.edges()

    for v in graph.vertex():
        T.add_vertex(v.coord, v.terrain, v.altitude)
        uf.make_set(v)

    print(liste_e)
    liste_e.sort(key=lambda x: (x[1][1]))
    for e in liste_e:
        if uf.find(e[0]) != uf.find(e[1][0]):
            v1 = T.get_vertetx(e[0].coord[0], e[0].coord[1])
            v2 = T.get_vertetx(e[1][0].coord[0], e[1][0].coord[1])
            T.add_edge(v1, v2, e[1][1])
            uf.union(e[0], e[1][0])

    return uf.parents

def chemin_kruskal(dic, sd, sa):
    list_final = [sa]
    vert = sa

    while dic[vert] != sd and dic[vert] != None:
        list_final.append(dic[vert])
        vert = dic[vert]

    list_final.append(sd)
    return list_final


def relachment(s1, s2):
    """
    :param s1: vertex 1
    :param s2: vertex 2
    :return:
    """
    pass


def dijsktra(graph, s):
    """
    :param graph: The graph we want to extract the shortest path
    :param s: the vertex of departure
    :return:
    """
    pred = {v: None for v in graph.vertex()}
    dist = {v: float("inf") for v in graph.vertex()}
    dist[s] = 0
    e = []
    f = set(graph.vertex())

    while len(f) != 0:
        si = min(f, key=lambda vert: dist[vert])
        f.remove(si)
        e.append(si)

        for sj in graph.succ(si):
            w = graph.get_weight(si, sj[0])
            if dist[sj[0]] > dist[si] + w:
                dist[sj[0]] = dist[si] + w
                pred[sj[0]] = si

    return pred

def chemin_dijkstra(dic, s):
    list_final = [s]
    vert = s

    while dic[vert] != None:
        list_final.append(dic[vert])
        vert = dic[vert]
    return list_final


def bellman_ford(graph, s):
    """
    :param graph: The graph we want to extract the shortest path
    :param s: the vertex of departure
    :return:
    """
    pred = {v: None for v in graph.vertex()}
    dist = {v: float("inf") for v in graph.vertex()}

    dist[s] = 0
    for k in range(1, len(graph.vertex()) - 1):
        for (si, sj) in graph.edges():
            print(si)
            if dist[sj[0]] > dist[si] + graph.get_weight(si, sj[0]):
                dist[sj[0]] = dist[si] + graph.get_weight(si, sj[0])
                pred[sj[0]] = si

    for (si, sj) in graph.edges():
        if dist[sj[0]] > dist[si] + graph.get_weight(si, sj[0]):
            print("On a un circuit absorbant")

    return pred


def floyd_warshal(graph):
    """

    :param graph: The graph we want to extract the shortest path
    :return:
    """
    pred = {v1: {v2: None for v2 in graph.vertex()} for v1 in graph.vertex()}
    dist = {v1: {v2: float('inf') for v2 in graph.vertex()} for v1 in graph.vertex()}
    for i in graph.vertex():
        dist[i][i] = 0
        for j in graph.succ(i):
            dist[i][j[0]] = j[1]
            pred[i][j[0]] = i

    for k in graph.vertex():
        for i in graph.vertex():
            for j in graph.vertex():
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


def text_graph(file):
    g = GraphList(True)
    f = open("image/" + file, "r")
    for line in f.readlines():
        v1, v2, l = line.split()
        if v1 not in g.vertex():
            g.add_vertex(v1)
        if v2 not in g.vertex():
            g.add_vertex(v2)
        g.add_edge(v1, v2, int(l))
    tstart = time.time()
    dist, pred = floyd_warshal(g)
    print(time.time() - tstart)
