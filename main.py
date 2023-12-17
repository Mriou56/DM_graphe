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


if __name__ == "__main__":
    # main()

    # CREATION D'UNE GRILLE 15x15
    hex_grid = HexGridViewer(16, 16)

    # test()
    # first_part(hex_grid)

    ## Algorithm to create a regular area around a vertex

    # question_zone(hex_grid)

    # Algorithm to create the longest river from a vertex

    # question_river(hex_grid)

    # build a map with constraint
    # nb Zone that we would like to add: nbRivers (max), nbZonesVolcan (max), nbZonesVilles, nbOtherZonesMax, maxDistance
    #carte_withConstraint(hex_grid, 2, 2, 2, 5, 4)

    # Create a map with the dijkstra algorithm to show the shortest route between cities

    # carte_dikjrsta(hex_grid, 10, 5)

    # Create a map with the kruskal algorithm to show the shortest route between cities

    # carte_kruskal(hex_grid, 10, 10)
