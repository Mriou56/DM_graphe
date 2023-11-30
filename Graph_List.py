# Importation
from abc import ABC, abstractmethod
from Graph import *
from Vertex import *
import random


class GraphList(Graph):

    def __init__(self, directed):
        super().__init__(directed)
        self.graph_dict = {}
        self.dict_elem = {'water': 1,
                          'path': 2,
                          'grass': 3,
                          'stone': 4,
                          'snow': 5,
                          'fire': 6,
                          'obsidian': 7
                          }

    def add_edge(self, vertex1:Vertex, vertex2:Vertex, label=None):
        """To add a new edge to the graph"""
        if label is not None:
            self.graph_dict[vertex1.coord].append((vertex2.coord, label))
            if not self.directed:
                self.graph_dict[vertex2.coord].append((vertex1.coord, label))

        else:
            self.graph_dict[vertex1.coord].append(vertex2.coord)
            if not self.directed:
                self.graph_dict[vertex2.coord].append(vertex1.coord)

    def add_vertex(self, coord, terrain, alt):
        """
        To add a new vertex to the graph
        :param coord: The coordinate of the vertex
        :param terrain: String of the type of terrain
        :param alt: The altitude of the vertex
        :return:
        """
        v = Vertex(coord, terrain, alt)
        self.graph_dict[v.coord] = []

    def has_edge(self, vertex1:Vertex, vertex2:Vertex, label=None):
        """Say if an edge between two vertex exist"""
        if label is not None:
            return (vertex2.coord, label) in self.graph_dict[vertex1.coord]
        else:
            return vertex2.coord in self.graph_dict[vertex1.coord]

    def vertex(self):
        """Return a list of all the vertex of a graph"""
        return self.graph_dict

    def label(self):
        """Return a list of all the label of each edges"""
        list_l = []
        for key in self.graph_dict:
            for k in self.graph_dict[key]:
                # print(k)
                list_l.append(k[1])
        return list_l

    def pred(self, vertex:Vertex):
        """ If a graph is directed
            Return a list of all the predecessor of a vertex"""
        list_pred = []
        for key in self.graph_dict:
            if vertex.coord in self.graph_dict[key]:
                list_pred.append(key)
        return list_pred

    def print(self):
        """Print the list of the graph"""
        for key in self.graph_dict:
            print("(vertex1: " + str(key) + "; vertex: " + str(self.graph_dict[key]) + ")")

    def succ(self, vertex:Vertex):
        """ If a graph is directed
            Return a list of all the successor of a vertex"""
        return self.graph_dict[vertex.coord]

    def cycled(self, ver:Vertex):
        """
        If a graph is a cycle
        :return: True
        """
        pred = {v: None for v in self.vertex()}
        vertex = [ver.coord]
        visited = set()
        visited.add(ver.coord)

        while vertex:

            u = vertex.pop(0)
            for v in self.succ(u):
                if isinstance(v, tuple):
                    if v[0] not in visited:
                        vertex.append(v[0])
                        visited.add(v[0])
                        pred[v[0]] = u
                    elif pred[u] != v[0]:
                        return True
                else:
                    if v not in visited:
                        vertex.append(v)
                        visited.add(v)
                        pred[v] = u
                    elif pred[u] != v:
                        return True
        return False

    def remove_edge(self, vertex1:Vertex, vertex2:Vertex, label=None):
        """
        Delete an edge from a graph
        :param vertex1: The first vertex of the edge
        :param vertex2: The last vertex of the edge
        :param label: The label of the edge
        :return: None
        """
        if label is not None:
            self.graph_dict[vertex1.coord].remove((vertex2.coord, label))
            if not self.directed:
                self.graph_dict[vertex2.coord].remove((vertex1.coord, label))

        else:
            self.graph_dict[vertex1.coord].remove(vertex2.coord)
            if not self.directed:
                self.graph_dict[vertex2.coord].remove(vertex1.coord)

    def get_weight(self, vertex1:Vertex, vertex2:Vertex):
        """
        Get the weight of an edge
        :param vertex1: The first vertex of the edge
        :param vertex2: The second vertex of the edge
        :return: The weight of the edge
        """
        tab_edge = self.edges()
        for e1, succs in tab_edge:
            for e2, label in succs:
                if (e1, e2) == (vertex1, vertex2):
                    return label
        raise Exception(f"vertex doen'st exists : ({vertex1}, {vertex2})")


    def get_neighbour(self, vertex:Vertex):
        """
        Get the neighbour of a vertex with it coordinates
        :param vertex: one vertex
        :return: the coordinates of the vertex next to the parameter's vertex
        """
        if vertex.coord[1] % 2 == 0:
            res = [(vertex.coord[0] + dx, vertex.coord[1] + dy) for dx, dy in ((1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))]
        else:
            res = [(vertex.coord[0] + dx, vertex.coord[1] + dy) for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1))]
        return [(dx, dy) for dx, dy in res if 0 <= dx < 15 and 0 <= dy < 15]
