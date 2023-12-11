# Importation
from abc import ABC, abstractmethod
from Graph import *
from Vertex import *
from Zone import *
from HexGridViewer import *
from Cercle import *
import random


## Dictionary for the area
dict_area = {'ville' : {0: 'gray', 1: 'gray', 2: 'gray', 3: 'gray', 4: 'darkolivegreen'},
             'desert' : {0: 'sandybrown', 1: 'sandybrown', 2:'sandybrown', 3:'sandybrown', 4:'sandybrown'},
             'foret' : {0:'darkgreen', 1:'forestgreen', 2:'forestgreen', 3:'forestgreen', 4:'forestgreen'},
             'montagne' : {0:'snow', 1:'linen', 2:'sienna', 3:'sienna', 4:'sienna'},
             'volcan' : {0:'red', 1:'darkred', 2:'darkred', 3:'saddlebrown', 4:'black'},
             'lagon' : {0:'turquoise', 1:'turquoise', 2:'turquoise', 3:'turquoise', 4:'aquamarine'}}



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
        """Return the dict where we have a list of all the vertex of a graph"""
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

    def get_neighbourold(self, x, y):
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

    def get_neighbour(self, v: Vertex):
        """
        Get the neighbour of a vertex v with it coordinates
        :param v: vertex (search his neighbour)


        reprendre dans le code du prof in res if 0 <= dx < self.__width and 0 <= dy < self.__height
        """
        list_v = []

        if v.coord[1] % 2 == 0:
            res = [(v.coord[0] + dx, v.coord[1] + dy) for dx, dy in
                   ((1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1))]
        else:
            res = [(v.coord[0] + dx, v.coord[1] + dy) for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1))]
        for vn in self.vertex():
            for dx, dy in res:
                if dx == vn.coord[0] and dy == vn.coord[1]:
                    list_v.append(vn)

        # temp - show items
        #       print("Voisin de : ", v.altitude)
        #       for i in list_v:
        #           print("> ", i.altitude)

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
        Get the higher vertex of the graph if several return a list
        :return:
        """
        # convert the dictionary items in a list and get the 1st items
        v_max = list(self.vertex())[0]
        max = v_max.altitude
        for v in self.vertex():
            if v.altitude > max:
                max = v.altitude
                v_max = v

        return v_max

    def find_ListOfhigher(self):
        """
        Get the list of higher vertex of the graph (same altitude)
        :return:
        """
        v_max = self.find_higher()
        mmax = [v_max]
        lVectWithoutOne = list(self.vertex())
        nb = 0
        nb2 = 0
        # loop to search all vertex with same altitude and add it in a list
        for v in lVectWithoutOne:
            nb2 = nb2 + 1
            if v.altitude == v_max.altitude:
                nb = nb + 1
                if v not in mmax:
                    mmax.add(v)
                    nb = nb + 1
        return mmax

    def zone(self, centre: Vertex, dist, dico: dict):
        """
        Get the area around a vertex
        :type centre: the center vertex
        :param dist: dist of the area
        :param dico: the dictionary of the corresponding area
        :return: zone of neighbor
        en partant d'un sommet,
        on va chercher à implémenter une zone autour de ce sommet.
        Cette zone sera de rayon dist. (exemple : si je pars du centre, il faut que je parcoure tous les sommets autours
        du centre puis les sommets autour des sommets du centre, etc).
       """
        queue = [(centre, 0)]
        visited = set()
        visited.add(centre)

        while queue:
            current_vertex, current_distance = queue.pop(0)
            current_vertex.terrain = dico[current_distance % 6]

            if current_distance < dist:
                neighbors = self.get_neighbour(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append((neighbor, current_distance + 1))
                        visited.add(neighbor)

    def zone2(self, centre: Vertex, dist, typeZone, dico: dict):
        """
        Get the area around a vertex
        :type centre: the center vertex
        :param dist: dist of the area
        :param dico: the dictionary of the corresponding area
        :return: zone of neighbors
       """
        queue = [(centre, 0)]
        zone=Zone(centre, dist,typeZone, dico)
        current_distance = 0
        visited = set()
        visited.add(centre)


        while queue:
            current_vertex, current_distance = queue.pop(0) # queue.pop(0)
            current_vertex.terrain = zone.areaDicoType[current_distance % 6]
            if zone.typeZone == 'ville' or zone.typeZone == 'foret':
                current_vertex.altitude = random.uniform(0.3, 0.6)
            else:
                if zone.typeZone == 'montagne' or zone.typeZone == 'volcan':
                    current_vertex.altitude = random.uniform(0.8, 1)
                else:
                    if zone.typeZone == 'desert':
                        current_vertex.altitude = random.uniform(0.4, 0.6)
                    else:
                        if zone.typeZone == 'lagon':
                            current_vertex.altitude = random.uniform(0.1, 0.3)

            if current_distance < dist:
                neighbors = self.get_neighbour(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append((neighbor, current_distance + 1))
                        zone.listVertexInTheZone.append((neighbor, current_distance + 1))
                        visited.add(neighbor)
                        if zone.typeZone == 'foret' or zone.typeZone == 'desert' or zone.typeZone == 'ville':
                            x = current_vertex.altitude - 0.2
                            y = current_vertex.altitude + 0.2
                            neighbor.altitude = random.uniform(x, y)
                        else:
                            if zone.typeZone == 'montagne' or zone.typeZone == 'volcan':
                                x = current_vertex.altitude - 0.1
                                y = current_vertex.altitude + 0.1
                                neighbor.altitude = random.uniform(x, y)
                            else:
                                if zone.typeZone == 'lagon':
                                    current_vertex.altitude = random.uniform(0.1, 0.3)
                                    neighbor.altitude = random.uniform(0.1, 0.3)

                        # Test if the altitude of the vertex is between 0 and 1
                        if neighbor.altitude >= 1:
                            neighbor.altitude = 1
                        else:
                            if neighbor.altitude <= 0.1:
                                neighbor.altitude = 0.1
        return zone

    def DFSinner(self, ver: Vertex, parcours: list):
        ver.terrain = "blue"
        min = []
        min_max = -1
        max = None

        for t in self.succ(ver):
            if t.altitude < ver.altitude:
                min.append(t)

        for i in min:
            if i.altitude > min_max:
                min_max = i.altitude
                max = i

        if max != None:
            parcours.append(max)
            self.DFSinner(max, parcours)

    def DFS(self, listVertNeigbour: [], vert: Vertex, path=None):
        """
        Return the longer path (can have several with the same distance)
        :param vert: Vertex
        :param listVertNeigbour: list of vertex neighbourg of vert
        """
        if path is None:
            path = [vert]
        paths = []
        paths_node = []
        for v in listVertNeigbour:
            if v.altitude <= vert.altitude:
                t_path = path + [v]
                paths_node.append(tuple(t_path))
                paths_node.extend(self.DFS(self.get_neighbour(v), v, t_path))


        if (len(paths_node) > 0):
            max_len = max(len(p) for p in paths_node)
            paths.extend([p for p in paths_node if len(p) == max_len])

        return paths

    # def riviere(self, vert: Vertex):
    def rivieres(self, listVertMaxAltitude: list):
        """
        From a list of Vertex, create for each one riviere
        :param listVertMaxAltitude: list of vertex having the altitude max
        :return: tab of tabs. each tab is a rivier path
        """
        # calcul path for a vertex (vert)
        # for each vertex (having same altitude) compare the length
        rivieres = []
        i=0
        for vM in listVertMaxAltitude:
            rivieres.append(self.riviere(vM))
        return rivieres

    def riviere(self, vert: Vertex):
        """
        Create a river from a vertex
        :param vert: start of river and search max path from this vertex
        :return: max path of riviere (if several paths with same longer return only one)
        """
        # calcul the longer path for a vertex (vert)
        all_paths = self.DFS(self.get_neighbour(vert), vert)
        if len(all_paths) > 0:
            max_len = max(len(p) for p in all_paths)
            all_maxpaths = [p for p in all_paths if len(p) == max_len]
            #  take only the 1st path (same if we have several path with the same length)
            for v in all_maxpaths[0]:
                v.terrain = 'royalblue'


            return all_maxpaths[0]
        else:
            return all_paths