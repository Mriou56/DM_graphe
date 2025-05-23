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


def first_part(hex_grid: HexGridViewer):
    """
    Function to answer to the question 1, 2, 3
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
    graphe_grid.zone(v, 3, dict_quest4)

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
        liste = graphe_grid.get_neighbour(v)
        for v2 in liste:
            graphe_grid.add_edge(v, v2)

    # get Max altitude
    listVertMax = graphe_grid.find_ListOfhigher(list(graphe_grid.vertex()))

    rivieres = []
    # show only one riviere in the graph
    rivieres = graphe_grid.rivieres(listVertMax)

    for v in graphe_grid.vertex():
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, value_edgecolor="black", show_altitude=True, debug_coords=False)


def carte_withConstraint(hex_grid: HexGridViewer, nbRivers, nbZonesVolcan, nbZonesVilles, nbOtherZonesMax, maxDistance):
    """
    Question 6 - Create a coherent card
    :type nbZonesVilles: nb Zones max that will be built
    :type nbZonesVolcan: nb volcan (constraint can t be on a ville and a river)
    :type nbRivers: nb max riviers (constraint can t be on a ville and a volcan)
    :param hex_grid: the grid to show
    :param nbOtherZonesMax: nb other zones that will be added (no constraint)
    :param maxDistance: distance max for a zone
    :return: build a graph
    """
    tab_ville = []

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

    # Ajout dans le Grid des biomes de manière aléatoire (les rivieres
    # ne sont pas des zones). Ne mets pas les volcans
    # On va modifier les zones en augmantant ou diminuant l'altide

    # dict_area_withoutConstraint dictionary where we have: ville,desert,foret,montage
    zones = []

    # Add the other zone (not Villes and not Volcan)
    # --------------------
    nbZoneCreated = 0
    while nbZoneCreated < nbOtherZonesMax:
        nbZoneCreated = nbZoneCreated + 1
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_height())
        v = graphe_grid.get_vertetx(x, y)
        d = random.randrange(1, maxDistance)
        # random with weight to define the type of biome (desert, foret or montain)
        biome = random.choices(tuple(dict_area_withoutVilleAndVolcan.keys()), weights=(3, 4, 2), k=1)
        zone = graphe_grid.zone2(v, d, biome[0], dict_area_withoutVilleAndVolcan[biome[0]])
        zones.append(zone)


    # Add the Zone villes
    # -------------------
    # list of all Vertex where we have a ville - avoid to have villes l'une sur l'autre, elles peuvent être voisine
    listVertexVilles = []
    listVertexToBeExluded = []
    nbVilleCreated = 0
    listVertexInzone = []
    nbZoneCreated = 0

    while nbVilleCreated < nbZonesVilles:
        d = random.randrange(1, maxDistance)  # 4
        zone = graphe_grid.zoneBuildWithConstraint(d, 'ville', listVertexToBeExluded, dict_ville)
        if zone is None:
            nbVilleCreated = nbZonesVilles
        else:
            nbVilleCreated = nbVilleCreated + 1
            listVertexInzone = zone.returnOnlyTheVertexs()
            listVertexToBeExluded = listVertexToBeExluded + listVertexInzone
            # add the listVertexInTheZone of this zone in the listVertexVilles
            listVertexVilles = listVertexVilles + listVertexInzone
            zones.append(zone)
            v = zone.getCentre()
            hex_grid.add_symbol(*v.coord, Circle("red"))
            tab_ville.append(v)



    #list used to build later the path, it will store all vertex where we can't put a path (volcan, rivier)
    listVertexToExcludeForPaths = []

    # build the volcan Zone (outside Ville zone and other volcan zone)
    # --------------
    nbZoneCreated = 0
    trouve = False
    listVertexVolcans = []
    listVertexToBeExluded = listVertexVilles

    while (nbZoneCreated < nbZonesVolcan):
        # positionne le 1er vertex du volcan sur une zone not ville

        # we try to build the volcan with a distance max  = d.
        # dès qu'un voisin n'est pas une ville, on l' ajoute si sa distance < d. Si tous les voisins sont des villes
        # ou limite du graphe, on arrete de construire le volcan
        d = random.randrange(1, 3)  # 4
        zone = graphe_grid.zoneBuildWithConstraint(d, 'volcan', listVertexToBeExluded, dict_volcan)
        if zone is None:
            nbZoneCreated = nbZonesVolcan
        else:
            nbZoneCreated = nbZoneCreated + 1
            listVertexInzone = zone.returnOnlyTheVertexs()
            # ListVertexToBeExluded.append(zone.returnOnlyTheVertexs)
            zones.append(zone)
            listVertexVolcans = listVertexVolcans + listVertexInzone
            listVertexToBeExluded = listVertexToBeExluded + listVertexInzone
            listVertexEcludeForPath = listVertexToBeExluded + listVertexVolcans

    # Creation of the rivers
    listStartRiversVertex = graphe_grid.find_higherVertexsForRiver(nbRivers, listVertexToBeExluded)
    if len(listStartRiversVertex) > 0:
        rivieresWithConstraint = graphe_grid.rivieresWithConstraint(listStartRiversVertex, listVertexToBeExluded)
    else:
        print("Not possible to add a river")

    # add in listVertexToExcludeForPaths the rivieres

    for riv in rivieresWithConstraint:
        for vert in riv:
            listVertexToExcludeForPaths.append(vert)


    # Buid the path - ville inside the "Ville" Zone
    for v1 in tab_ville:
        for v2 in tab_ville:
            # Get the address of the vertex in the graph grid
            vertex1 = graphe_grid.get_vertetx(*v1.coord)
            vertex2 = graphe_grid.get_vertetx(*v2.coord)

            # Get the shortest path between two towns in the grid
            # tstart = time.time()
            short = pcc(graphe_grid, vertex1, vertex2)
            # print(time.time() - tstart)
            for x in range(0, len(short) - 1):
                hex_grid.add_link(short[x].coord, short[x + 1].coord, "purple")

    # End of treatment - add colors...
    # -------------------
    for v in graphe_grid.vertex():
        # Modification of the color and the opacity of one cell
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    hex_grid.show(alias={"royalblue": "water", "snow": "snow", "gray": "town", "sandybrown": "desert",
                         "darkolivegreen": "périphérie",
                         "darkgreen": "foret", "forestgreen": "foret", "linen": "montagne", "sienna": "montagne",
                         "red": "lava",
                         "darkred": "lava", "saddlebrown": "obscidian", "black": "obsidian", "turquoise": "lagon",
                         "green": "grass"}, show_altitude=True,
                  debug_coords=False)


def carte_old(hex_grid: HexGridViewer, nb_rivers, nb_zones):
    """
    Question 6 - Create a coherent card
    :param hex_grid: the grid to show
    :param nb_zones: that we want to have
    :return:
    """
    tab_ville = []

    # calcule max distance - that is linked to hex_grid.width and height
    if hex_grid.get_width() > hex_grid.get_height():
        # take height as reference
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
    # ne sont pas des zones). Ne mets pas les volcans
    # On va modifier les zones en augmantant ou diminuant l'altide

    # dict_area_withoutConstraint dictionary where we have: ville,desert,foret,montage
    zonesDesVilles = []
    zones = []
    for n in range(0, nb_zones):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_width())
        v = graphe_grid.get_vertetx(x, y)
        d = random.randrange(1, 4)
        # random with weight to define the type of biome (villes ou desert ...)
        biome = random.choices(tuple(dict_area.keys()), weights=(9, 3, 5, 4, 2, 2), k=1)
        zone = graphe_grid.zone2(v, d, biome[0], dict_area[biome[0]])
        zones.append(zone)
        # graphe_grid.zone2(v, d, dict_area[biome[0]])

        if biome[0] == 'ville':
            hex_grid.add_symbol(*v.coord, Circle("red"))
            tab_ville.append(v)
            # add the zone in the zonesDesVilles
            zonesDesVilles.append(zone)

    ttotal = 0
    for v1 in tab_ville:
        for v2 in tab_ville:
            # Get the address of the vertex in the graph grid
            vertex1 = graphe_grid.get_vertetx(*v1.coord)
            vertex2 = graphe_grid.get_vertetx(*v2.coord)

            # Get the shortest path between two towns in the grid
            tstart = time.time()
            short = pcc(graphe_grid, vertex1, vertex2)
            ttotal += time.time() - tstart
            for x in range(0, len(short) - 1):
                hex_grid.add_link(short[x].coord, short[x + 1].coord, "purple")

    print('Le temps de parcours du plus court chemin ==>', ttotal)

    # Creation of the rivers
    for n in range(0, nb_rivers):
        x = random.randrange(0, hex_grid.get_width())
        y = random.randrange(0, hex_grid.get_height())
        v = graphe_grid.get_vertetx(x, y)
        graphe_grid.riviere(v)

    # put the Volcan (size 1 and 4) can 't be on a Ville and a River

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


def carte_dikjrsta(hex_grid, nb_zone, nb_river):
    """
    Show a card with the shortest path between each city
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
            if dist < 0:
                dist = -dist
                graphe_grid.add_edge(v, v2, dist)
            else:
                graphe_grid.add_edge(v, v2, dist)
            # Verification of the practicality of the terrain
            if v.terrain == 'royalblue' or v.terrain == 'red' or v.terrain == 'turquoise':
                graphe_grid.remove_edge(v, v2, dist)

    ttotal = 0
    # Use the dijkstra algorithme to search the shortest path between two cities
    for v1 in tab_ville:
        for v2 in tab_ville:
            if v1 != v2:

                tstart = time.time()
                short = dijsktra(graphe_grid, v1)
                ttotal += time.time() - tstart
                list_short = chemin_dijkstra(short, v2)

                # Show the link between vertex
                for x in range(0, len(list_short) - 1):
                    hex_grid.add_link(list_short[x].coord, list_short[x + 1].coord, "purple")

    print('Le temps de parcours de Dijkstra =>', ttotal)

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


def carte_kruskal(hex_grid, nb_zone, nb_river):
    """
    Show a card with the shortest path between each city with the kruskal algorithme
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
                               k=1)  # weights for the moderation and k for the len of the list
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
        listN = graphe_grid.get_neighbour(v)
        for v2 in listN:
            dist = dict_dist[v2.terrain] + (v.altitude - v2.altitude)
            if dist < 0:
                dist = -dist
                graphe_grid.add_edge(v, v2, dist)
            else:
                graphe_grid.add_edge(v, v2, dist)
            # Verification of the practicality of the terrain
            if v.terrain == 'royalblue' or v.terrain == 'red' or v.terrain == 'turquoise':
                graphe_grid.remove_edge(v, v2, dist)

    # Create an undergraph with all the cities
    gville = GraphList(False)
    for v in tab_ville:
        gville.add_vertex(v.coord, v.terrain, v.altitude)

    dict_chemin = {}

    # Use the dijkstra algorithme to search the shortest path between two cities
    for v1 in tab_ville:
        for v2 in tab_ville:
            if v1 != v2:
                short = dijsktra(graphe_grid, v1)
                list_short = chemin_dijkstra(short, v2)

                w = 0
                ville1 = gville.get_vertetx(v1.coord[0], v1.coord[1])
                ville2 = gville.get_vertetx(v2.coord[0], v2.coord[1])
                dict_chemin[(ville1, ville2)] = list_short

                # Show the link between vertex
                for x in range(0, len(list_short) - 1):
                    e1 = graphe_grid.get_vertetx(list_short[x].coord[0], list_short[x].coord[1])
                    e2 = graphe_grid.get_vertetx(list_short[x + 1].coord[0], list_short[x + 1].coord[1])
                    w += graphe_grid.get_weight(e1, e2)

                gville.add_edge(ville1, ville2, w)

    # Use the kruskal algorithme to search the shortest path between two cities
    tstart = time.time()
    cheminK = kruskal_UF(gville)
    print('Le temps de parcours de Kruskal =>', time.time() - tstart)

    # print(cheminK)
    for k, v in cheminK.items():
        if v is not None:
            for e in range(0, len(dict_chemin[(k, v)]) - 1):
                hex_grid.add_link(dict_chemin[(k, v)][e].coord, dict_chemin[(k, v)][e + 1].coord, "purple")

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