# Importation
from abc import ABC, abstractmethod


# Class


class Graph(ABC):

    def __init__(self, directed=False):
        self.directed = directed

    @abstractmethod  # decorator to say the next method is abstract
    # To add a new vertex (=sommet) to the graph => None
    def add_vertex(self, coord, terrain, alt):
        """To add a new edge to the graph"""
        pass

    @abstractmethod
    def add_edge(self, vertex1, vertex2, label=None):
        """To add a new vertex to the graph"""
        pass

    def adj(self, vertex):
        """Return a list of adjacent vertex of one vertex"""
        list_v = self.vertex()
        list_adj = []
        for i in list_v:
            if self.has_edge(vertex, i):
                list_adj.append(i)
        return list_adj

    def degree(self, vertex=None, sign="+"):
        """Return the degree of a vertex"""
        return len(self.adj(vertex))

    def edges(self):
        """Return a tuple list which match with the two vertex of one edge with all the edges of the graph"""
        """Peut-être prendre la mienne a l'avenir qui est tout de même plus optimisé"""
        list_v = self.vertex()
        list_e = []
        list_l = self.label()
        for i in list_v:
            for j in list_v:
                if self.has_edge(i, j):
                    list_e.append((i, j))
                if list_l is not None:
                    for h in list_l:
                        if self.has_edge(i, j, h) and (i, (j, h)) not in list_e:
                            list_e.append((i, (j, h)))

        return list_e

    @abstractmethod
    def has_edge(self, vertex1, vertex2, label=None):
        """Say if an edge between two vertex exist"""
        pass

    def is_directed(self):
        """Say if the graphe is directed"""
        return self.directed

    @abstractmethod
    def vertex(self):
        """Return a list of all the vertex of a graph"""
        pass

    @abstractmethod
    def label(self):
        """Return a list of all the label of each edges"""
        pass

    @abstractmethod
    def pred(self, vertex):
        """ If a graph is directed
            Return a list of all the predecessor of a vertex"""
        pass

    @abstractmethod
    def print(self):
        """Print the graph"""
        pass

    @abstractmethod
    def succ(self, vertex):
        """ If a graph is directed
            Return a list of all the successor of a vertex"""
        pass

    @abstractmethod
    def cycled(self, v):
        """
        If a graph is a cycle
        :return: True
        """
        pass

    @abstractmethod
    def remove_edge(self, vertex1, vertex2, label=None):
        """
        Delete an edge from a graph
        :param vertex1: The first vertex of the edge
        :param vertex2: The last vertex of the edge
        :param label: The label of the edge
        :return: None
        """
        pass

    @abstractmethod
    def get_weight(self, vertex1, vertex2):
        """
        Get the weight of an edge
        :param vertex1: The first vertex of the edge
        :param vertex2: The second vertex of the edge
        :return: The weight of the edge
        """
        pass
    @abstractmethod
    def get_neighbour(self, vertex):
        """
        Get the neighbour of a vertex with it coordinates
        :param vertex: one vertex
        :return: the coordinates of the vertex next to the parameter's vertex
        """
        pass
