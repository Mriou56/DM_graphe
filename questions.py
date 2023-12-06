from __future__ import annotations

import random

from Graph_List import *

from HexGridViewer import *
from Cercle import *
from Rect import *

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
    for i in range(0, 15):
        for j in range(0, 15):
            t = random.choice(graphe_grid.dict_elem)
            alt = random.randrange(2, 10)
            graphe_grid.add_vertex((i, j), t, alt)

    for v in graphe_grid.vertex():
        # ADD EDGES BETWEEN VERTEX
        list = graphe_grid.get_neighbour(v.coord[0], v.coord[1])
        for v2 in list:
            graphe_grid.add_edge(v, v2)

        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v.coord[0], v.coord[1], v.terrain)
        hex_grid.add_alpha(v.coord[0], v.coord[1], v.altitude/10)

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
    for i in range(0, 15):
        for j in range(0, 15):
            t = 'snow'
            alt = 1
            graphe_grid.add_vertex((i, j), t, alt)

    v = graphe_grid.get_vertetx(5,5)
    graphe_grid.zone(v, 4)

    for v in graphe_grid.vertex():
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v.coord[0], v.coord[1], v.terrain)
        hex_grid.add_alpha(v.coord[0], v.coord[1], v.altitude)

    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=False, debug_coords=True)

def question_river(hex_grid: HexGridViewer):
    """
    Test for the creation of a river
    :param hex_grid: the grid to show
    :return:
    """
    # CREATION D'UN GRAPHE
    graphe_grid = GraphList(False)
    for i in range(0, 15):
        for j in range(0, 15):
            t = 'snow'
            alt = 0.4
            graphe_grid.add_vertex((i, j), t, alt)

    vert = graphe_grid.get_vertetx(4, 8 )
    v1 = graphe_grid.get_vertetx(4,9)
    v2 = graphe_grid.get_vertetx(5,10)
    v3 =  graphe_grid.get_vertetx(6,10)
    v4 = graphe_grid.get_vertetx(7,10)

    vert.altitude = 1
    v1.altitude = 0.9
    v2.altitude = 0.8
    v3.altitude = 0.7
    v4.altitude = 0.6


    for v in graphe_grid.vertex():
        # ADD EDGES BETWEEN VERTEX
        list = graphe_grid.get_neighbour(v.coord[0], v.coord[1])
        for v2 in list:
            graphe_grid.add_edge(v, v2)

    graphe_grid.rivière(vert)

    for v in graphe_grid.vertex():
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v.coord[0], v.coord[1], v.terrain)
        hex_grid.add_alpha(v.coord[0], v.coord[1], v.altitude)


    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=False, debug_coords=True)

def carte(hex_grid : HexGridViewer, nb_rivers, nb_zones):
    """
    Create a coherent card
    :param hex_grid: the grid to show
    :return:
    """
    # Creation of a graph
    graphe_grid = GraphList(False)
    for i in range(0, 15):
        for j in range(0, 15):
            t = 'forestgreen'
            alt = 1 # Voir comment gérer les altitudes pour que se soit beau
            graphe_grid.add_vertex((i, j), t, alt)


    for v in graphe_grid.vertex():
        # Add edges between vertex of the graph
        list = graphe_grid.get_neighbour(v.coord[0], v.coord[1])
        for v2 in list:
            graphe_grid.add_edge(v, v2)

    # Creation of the rivers
    for n in range (0, nb_rivers):
        x = random.randrange(0,15)
        y = random.randrange(0, 15)
        v = graphe_grid.get_vertetx(x, y)
        graphe_grid.rivière(v)

    # Creation of area
    for n in range (0, nb_zones):
        x = random.randrange(0, 15)
        y = random.randrange(0, 15)
        v = graphe_grid.get_vertetx(x, y)
        d = random.randrange(2, 6)
        graphe_grid.zone(v, d)


    for v in graphe_grid.vertex():
        # Modification of the color and the opacity of one cell
        hex_grid.add_color(v.coord[0], v.coord[1], v.terrain)
        hex_grid.add_alpha(v.coord[0], v.coord[1], v.altitude)

    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=False, debug_coords=True)

