"""
Programme basique en python3.8 permettant via matplolib de visualiser une grille hexagonale.

Elle propose simplement:
 - l'affichage des hexagones, avec des couleurs et une opacité
 - l'ajout de formes colorées sur les hexagones
 - l'ajout de liens colorés entre les hexagones

Contact: sebastien.gamblin@isen-ouest.yncrea.fr
"""

from __future__ import annotations

from questions import *


# il y a mieux en python :
# - 3.11: Coords: AliasType = Tuple[int, int]
# - 3.12: type Coords = Tuple[int, int]


if __name__ == "__main__":
    # main()

    # CREATION D'UNE GRILLE 15x15
    hex_grid = HexGridViewer(15, 15)

    # test()
    #question_1(hex_grid)

    ## Quel algorithme utiliser pour générer une zone régulière qui s'étend sur la carte (i.e. toutes les cases à
    # distance $i$ d'une case)?

    # question_zone(hex_grid)

    ## Quel algorithme permettrait de tracer des rivières à partir d'un point donné sur la carte, en ajoutant une
    # contrainte d'altitude descendante en prenannt le chemin le plus long possible ?

    '''Le mieux est de s'inspirer du code du DFS'''

    # question_river(hex_grid)


    # Algo pour faire une carte jolie

    #carte(hex_grid, 5, 10)
    """
    Tests de temps
    Grille 15x15 et 5 villes => 0.004   et 10 villes => 004
    Grille 50x50 et 5 villes=> 0.5      et 10 villes => 0.5
    Grille 90x90 et 5 villes => 5.6     et 10 villes => 5.6
    """

    ## Quel algorithme utiliser pour aller d'un point A à un point B ?



    ## Quel algorithme utiliser pour créer un réseau de routes le moins couteux possible entre x villes, pour qu'elles
    # sont toutes interconnectées ?

    '''g = GraphList(False)

    g.add_vertex((0,1), 'blue', 0.1)
    g.add_vertex((1, 1), 'blue', 0.1)
    g.add_vertex((3, 1), 'blue', 0.1)
    g.add_vertex((3, 2), 'blue', 0.1)
    v1 = g.get_vertetx(0,1)
    v2 = g.get_vertetx(1,1)
    v3 = g.get_vertetx(3,1)
    v4 = g.get_vertetx(3, 2)
    g.add_edge(v1, v2, 4)
    g.add_edge(v1, v3, 5),
    g.add_edge(v3, v2, 7)
    g.add_edge(v3, v4, 2)
    g.add_edge(v1, v4, 1)

    p = g.get_weight(v1, v3)'''

    carte_dikjrsta(hex_grid, 5, 10)





