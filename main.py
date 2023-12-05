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

    # question_1(hex_grid)


    ## Quel algorithme utiliser pour générer une zone régulière qui s'étend sur la carte (i.e. toutes les cases à
    # distance $i$ d'une case)?

    # question_zone(hex_grid)

    ## Quel algorithme permettrait de tracer des rivières à partir d'un point donné sur la carte, en ajoutant une
    # contrainte d'altitude descendante en prenannt le chemin le plus long possible ?

    question_river(hex_grid)

    ## Quel algorithme utiliser pour aller d'un point A à un point B ?

    ## Quel algorithme utiliser pour créer un réseau de routes le moins couteux possible entre x villes, pour qu'elles
    # sont toutes interconnectées ?


