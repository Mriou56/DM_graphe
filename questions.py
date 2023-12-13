from __future__ import annotations

import random
import time

from Graph_List import *

from HexGridViewer import *
from Cercle import *
from Rect import *
from Tri import *


def test():
    """
    Fonction exemple pour présenter le programme ci-dessus.
    """
    # CREATION D'UNE GRILLE 15x15
    hex_grid = HexGridViewer(15, 15)

    # MODIFICATION DE LA COULEUR D'UNE CASE
    # hex_grid.add_color(X, Y, color) où :
    # - X et Y sont les coordonnées de l'hexagone et color la couleur associée à cet hexagone.
    hex_grid.add_color(5, 5, "purple")
    hex_grid.add_color(1, 0, "red")

    # MODIFICATION DE LA TRANSPARENCE D'UNE CASE
    # hex_grid.add_alpha(X, Y, alpha) où :
    # - X et Y sont les coordonnées de l'hexagone et alpha la transparence associée à cet hexagone.
    hex_grid.add_alpha(5, 5, 0.7)

    # RECUPERATION DES VOISINS D'UNE CASE : ils sont entre 2 et 6.
    # hex_grid.get_neighbours(X, Y)

    for _x, _y in hex_grid.get_neighbours(5, 5):
        hex_grid.add_color(_x, _y, "blue")
        hex_grid.add_alpha(_x, _y, random.uniform(0.2, 1))

    for _x, _y in hex_grid.get_neighbours(1, 0):
        hex_grid.add_color(_x, _y, "pink")
        hex_grid.add_alpha(_x, _y, random.uniform(0.2, 1))

    # AJOUT DE SYMBOLES SUR LES CASES : avec couleur et bordure
    # hex_grid.add_symbol(X, Y, FORME)
    hex_grid.add_symbol(10, 8, Circle("red"))
    hex_grid.add_symbol(9, 8, Rect("green"))
    hex_grid.add_symbol(3, 4, Rect("pink", edgecolor="black"))

    # AJOUT DE LIENS ENTRE LES CASES : avec couleur
    hex_grid.add_link((5, 5), (6, 6), "red")
    hex_grid.add_link((8, 8), (7, 8), "purple", thick=4)

    # AFFICHAGE DE LA GRILLE
    # alias permet de renommer les noms de la légende pour des couleurs spécifiques.
    # debug_coords permet de modifier l'affichage des coordonnées sur les cases.
    hex_grid.show(alias={"blue": "water", "white": "void", "grey": "rock"}, debug_coords=False)


def question_1(hex_grid: HexGridViewer):
    """
    Function to anser to the question 1, 2, 3
    :param hex_grid:
    :return:
    """
    # CREATION D'UN GRAPHE
    graphe_grid = GraphList(False)
    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = random.choice(graphe_grid.dict_elem)
            alt = random.uniform(0.2, 1)
            graphe_grid.add_vertex((i, j), t, alt)

    for v in graphe_grid.vertex():
        # ADD EDGES BETWEEN VERTEX
        list = graphe_grid.get_neighbour(v)
        for v2 in list:
            graphe_grid.add_edge(v, v2)

        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    # AFFICHAGE DE LA GRILLE
    # alias permet de renommer les noms de la légende pour des couleurs spécifiques.
    # debug_coords permet de modifier l'affichage des coordonnées sur les cases.
    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=True, debug_coords=False)


def question_zone(hex_grid: HexGridViewer):
    """
    Function to create a zone around a vertex
    :param hex_grid: a grid
    :return:
    """
    # CREATION D'UN GRAPHE
    graphe_grid = GraphList(False)
    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = 'snow'
            alt = 1
            graphe_grid.add_vertex((i, j), t, alt)

    v = graphe_grid.get_vertetx(5, 5)
    graphe_grid.zone(v, 4, dict_area['foret'])

    for v in graphe_grid.vertex():
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, value_edgecolor="black", show_altitude=False, debug_coords=False)


def question_river(hex_grid: HexGridViewer):
    """
    Question 5 -  for the creation of a river
    :param hex_grid: the grid to show
    :return:
    """
    # CREATION D'UN GRAPHE
    graphe_grid = GraphList(False)
    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = 'snow'
            alt = random.uniform(0.2, 1)
            graphe_grid.add_vertex((i, j), t, alt)

    # add edge (arrête) entre les Vertex
    for v in graphe_grid.vertex():
        list = graphe_grid.get_neighbour(v)
        for v2 in list:
            graphe_grid.add_edge(v, v2)

    # get Max altitude
    listVertMax = graphe_grid.find_ListOfhigher()

    rivieres = []
    # show only one riviere in the graph
    rivieres=graphe_grid.rivieres(listVertMax)


    for v in graphe_grid.vertex():
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, value_edgecolor="black", show_altitude=True, debug_coords=False)


def carte(hex_grid: HexGridViewer, nb_rivers, nb_zones):
    """
    Question 6 - Create a coherent card
    :param hex_grid: the grid to show
    :param nb_zones: that we want to have
    :return:
    """
    tab_ville = []

    #calcule max distance - that is linked to hex_grid.width and height
    if hex_grid.get_width() >  hex_grid.get_height():
        #take height as reference
        max_distance = int(hex_grid.get_height() / 4)
    else:
        max_distance = int(hex_grid.get_width() / 4)
    if max_distance < 2:
        max_distance = 2

    # Creation of a graph - all is green
    # positionnement zone de plaine dans le Graph
    graphe_grid = GraphList(False)
    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = 'green'
            alt = random.uniform(0.2, 0.5)
            graphe_grid.add_vertex((i, j), t, alt)

    # add edge (arrête) entre les Vertex
    for v in graphe_grid.vertex():
        # Add edges between vertex of the graph
        list = graphe_grid.get_neighbour(v)
        for v2 in list:
            graphe_grid.add_edge(v, v2)

    # Modification for a logical altitude
    '''list_N = graphe_grid.get_neighbour(i, j)
    a = 0
    if len(list_N) > 1:
        for n in list_N:
            a += n.altitude
        v = graphe_grid.get_vertetx(i, j)
        v.altitude = a / len(list_N)
        print(v.altitude)'''

    # Ajout dans le Grid des zones (biomes)de manière aléatoire - zone de type eau, sable, glace, ville (les rivieres
    # ne sont pas des zones
    # On va modifier les zones en augmantant ou diminuant l'altide

    zones = []
    for n in range(0, nb_zones):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_width())
        v = graphe_grid.get_vertetx(x, y)
        d = random.randrange(1, max_distance)
        # random with weight to define the type of biome (villes ou desert ...)
        biome = random.choices(tuple(dict_area.keys()), weights=(9,3,5,4,2,2), k=1)
        zone = graphe_grid.zone2(v, d, biome[0], dict_area[biome[0]])
        zones.append(zone)
        #graphe_grid.zone2(v, d, dict_area[biome[0]])

        if biome[0] == 'ville':
            hex_grid.add_symbol(*v.coord, Circle("red"))
            tab_ville.append(v)


    for v1 in tab_ville:
        for v2 in tab_ville:
            # Get the address of the vertex in the graph grid
            vertex1 = graphe_grid.get_vertetx(*v1.coord)
            vertex2 = graphe_grid.get_vertetx(*v2.coord)

            # Get the shortest path between two towns in the grid
            #tstart = time.time()
            short = pcc(graphe_grid, vertex1, vertex2)
            #print(time.time() - tstart)
            for x in range(0,len(short)-1):
                hex_grid.add_link(short[x].coord, short[x+1].coord, "purple")



    # Creation of the rivers
    for n in range(0, nb_rivers):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_height())
        v = graphe_grid.get_vertetx(x, y)
        graphe_grid.riviere(v)

    for v in graphe_grid.vertex():
        # Modification of the color and the opacity of one cell
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)
       # hex_grid.add_color(v.coord[0], v.coord[1], v.terrain)
       # hex_grid.add_alpha(v.coord[0], v.coord[1], v.altitude)

    hex_grid.show(alias={"royalblue": "water", "snow": "snow", "gray": "town", "sandybrown": "desert",
                         "darkolivegreen": "périphérie",
                         "darkgreen": "foret", "forestgreen": "foret", "linen": "montagne", "sienna": "montagne",
                         "red": "lava",
                         "darkred": "lava", "saddlebrown": "obscidian", "black": "obsidian", "turquoise": "lagon", "green":"grass"},
                  debug_coords=False)

def carte_dikjrsta(hex_grid, nb_zone, nb_river):
    """
    Show a card with the shortest path between each cities
    :param hex_grid:
    :param nb_zone: the number of area we want in the graph
    :param nb_river: the number of rivers we want in the grid
    :return:
    """
    tab_ville = []
    # Creation of a graph - all is green
    graphe_grid = GraphList(True)

    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = 'green'
            alt = random.uniform(0.2, 0.5)
            graphe_grid.add_vertex((i, j), t, alt)

    zones = []
    for n in range(0, nb_zone):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_width())
        v = graphe_grid.get_vertetx(x, y)
        d = random.randrange(1, 5)
        biome = random.choices(tuple(dict_area.keys()), weights=(9, 3, 5, 4, 2, 2),
                               k=1)  # weights for the ponderation and k for the len of the list
        zone = graphe_grid.zone2(v, d, biome[0], dict_area[biome[0]])
        zones.append(zone)
        # graphe_grid.zone2(v, d, dict_area[biome[0]])

        if biome[0] == 'ville':
            hex_grid.add_symbol(*v.coord, Circle("red"))
            tab_ville.append(v)

    # Creation of the rivers
    for n in range(0, nb_river):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_height())
        v = graphe_grid.get_vertetx(x, y)
        graphe_grid.riviere(v)

    # add edge (arrête) entre les Vertex
    for v in graphe_grid.vertex():
        # Add edges between vertex of the graph
        list = graphe_grid.get_neighbour(v)
        for v2 in list:
            dist = dict_dist[v2.terrain] + (v.altitude - v2.altitude)
            graphe_grid.add_edge(v, v2, dist)
            # Verification of the practicality of the terrain
            if v.terrain == 'royalblue' or v.terrain == 'red' or v.terrain == 'turquoise':
                graphe_grid.remove_edge(v, v2, dist)

    # Use the dijkstra algorithme to search the shortest path between two cities
    for v1 in tab_ville:
        print(v1)
        # Get the address of the vertex in the graph grid
        vertex1 = graphe_grid.get_vertetx(*v1.coord)

        # Get the shortest path between two towns in the grid
        tstart = time.time()
        short = dijsktra(graphe_grid, vertex1)
        print(time.time() - tstart)
        for x in range(0,len(short)-1):
            hex_grid.add_link(short[x].coord, short[x+1].coord, "pink")

    for v in graphe_grid.vertex():
        # Modification of the color and the opacity of one cell
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    hex_grid.show(alias={"royalblue": "water", "snow": "snow", "gray": "town", "sandybrown": "desert",
                         "darkolivegreen": "périphérie",
                         "darkgreen": "foret", "forestgreen": "foret", "linen": "montagne", "sienna": "montagne",
                         "red": "lava",
                         "darkred": "lava", "saddlebrown": "obscidian", "black": "obsidian", "turquoise": "lagon",
                         "green": "grass"},
                  debug_coords=False)
