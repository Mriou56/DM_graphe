# Importation
from abc import ABC, abstractmethod
from Graph import *
from Vertex import *
from HexGridViewer import *
import random


class GraphList(Graph):

    def __init__(self, directed):
        super().__init__(directed)
        self.graph_dict = {}
        self.dict_elem = ['royalblue', 'chocolate', 'forestgreen', 'grey', 'snow', 'red', 'black']

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, label=None):
        """To add a new edge to the graph"""
        if label is not None:
            self.graph_dict[vertex1.coord].append((vertex2.coord, label))
            if not self.directed:
                self.graph_dict[vertex2.coord].append((vertex1.coord, label))

        else:
            self.graph_dict[vertex1].append(vertex2)
            if not self.directed:
                self.graph_dict[vertex2].append(vertex1)

    def add_vertex(self, coord, terrain, alt):
        """
        To add a new vertex to the graph
        :param coord: The coordinate of the vertex
        :param terrain: String of the type of terrain
        :param alt: The altitude of the vertex
        :return:
        """
        v = Vertex(coord, terrain, alt)
        self.graph_dict[v] = []

    def has_edge(self, vertex1: Vertex, vertex2: Vertex, label=None):
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

    def pred(self, vertex: Vertex):
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

    def succ(self, vertex: Vertex):
        """ If a graph is directed
            Return a list of all the successor of a vertex"""
        return self.graph_dict[vertex]

    def cycled(self, ver: Vertex):
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

    def remove_edge(self, vertex1: Vertex, vertex2: Vertex, label=None):
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


    def get_weight(self, vertex1: Vertex, vertex2: Vertex):
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


    def get_neighbour(self, x, y):
        """
        Get the neighbour of a vertex with it coordinates
        :param x: abscissa coordinate of the vertex
        :param y: ordinate coordinate of the vertex
        :return: the coordinates of the vertex next to the parameter's vertex

        reprendre dans le code du prof in res if 0 <= dx < self.__width and 0 <= dy < self.__height
        """
        list_v = []

        if y % 2 == 0:
            res = [(x + dx, y + dy) for dx, dy in ((1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))]
        else:
            res = [(x + dx, y + dy) for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1))]
        for v in self.vertex():
            for dx, dy in res:
                if dx == v.coord[0] and dy == v.coord[1]:
                    list_v.append(v)

        return list_v

    def get_vertetx(self, x, y):
        """
        Get the corresponding vertex of the graph
        :param x: The abscissa coordinate
        :param y: The ordinate coordinate
        :return:
        """
        list_V = self.vertex()
        v_final = None
        for vert in list_V:
            if vert.coord[0] == x and vert.coord[1] == y:
                v_final = vert

        return v_final
    def find_higher(self):
        """
        Get the higher vertex of the graph
        :return:
        """
        max = 0
        v_max = None
        for v in self.vertex():
            if v.alt > max:
                max = v.alt
                v_max = v
        return v_max

    def zone(self, v: Vertex, dist):
        """
        Get the area around a vertex
        :param dist: dist of the area
        :param v: the center vertex
        :return: zone of neighboor
        """

        n = 0
        v.terrain = 'black'
        dic_color = {0: "black", 1: "red", 2: "orange", 3: "yellow", 4: "pink", 5:'purple'}
        neighbour = [v]

        def color_n(voisins, color):
            for next in voisins:
                if next.terrain == 'snow':
                    next.terrain = color
                    neighbour.append(next)

        color_n(self.get_neighbour(neighbour[0].coord[0], neighbour[0].coord[1]), dic_color[n+1])
        while n < dist:
            n += 1
            v = self.get_neighbour(neighbour[0].coord[0], neighbour[0].coord[1])
            print(v)
            for next in v:
                print(next.coord)
                color_n(self.get_neighbour(next.coord[0], next.coord[1]), dic_color[n+1])
                neighbour.pop(0)

        '''
        Ton code, je teste autre chose, ca marche pas bien j'ai une grille toute rouge
        n = 0
        list_neighboor = [v]
        dic_color = {0: "black", 1: "red", 2:"orange", 3:"yellow"}
        file = [v]
        v.terrain = dic_color[n]
        while n < dist:
            for x in self.get_neighbour(file[0].coord[0], file[0].coord[1]):
                if x in list_neighboor:
                    pass
                else:
                    list_neighboor.append(x)
                    if x.terrain == 'snow':
                        x.terrain = dic_color[n+1]
                    #x.printV()
                    file.append(x)
            file.pop(0)
            n += 1
        '''
    def rivière(self, vert: Vertex):
        """
        Create a river from a vertex
        :param vert: The vertex of the beginning
        :return:
        """
        parcours = [vert]

        def DFSinner(ver):
            ver.terrain = "royalblue"
            min = []
            min_max = 0
            max = None
            for t in self.succ(ver):
                if t.altitude < ver.altitude:
                    min.append(t)
                    DFSinner(t)

            for i in min:
                if i.altitude > min_max:
                    min_max = i.altitude
                    max = i


            if max != None:
                parcours.append(max)

        if vert is not None:
            DFSinner(vert)
        else:
            for v in self.vertex():
                if v.terrain == "snow":
                    DFSinner(v)
        print(parcours)
        for v in parcours:
            v.terrain = 'royalblue'


