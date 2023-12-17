# Devoir maison graphe

## Introduction :

Au sein de notre parcours en tant qu'élève en ingénierie à l'ISEN de Caen,
nous avons dû effectuer un devoir maison en théorie des graphes.
Notre tâche consistait à modéliser une zone géographique en deux dimensions,
exploitant un code source initial fourni par notre professeur.
L'utilisation de la bibliothèque Python, Matplotlib et Pyplot, a facilité la représentation visuelle de notre modèle.

La structure des TP que nous avions réalisé en cours
nous a permis de répondre plus facilement aux questions demandées.
Afin de faciliter la communication et le travail d'équipe,
nous avons opté pour l'utilisation de Github.
Cette plateforme nous a permis de suivre les contributions individuelles de chacun lorsque nous n'étions pas ensemble.
Nous avons aussi travaillé après les cours ou sur discord lorsque l'on était tous les deux disponible et quand nous avions des problèmes sur une fonction,
l'utilisation de code together nous a permis de travailler ensemble sur un seul et même code.

Ce rapport a pour objectif de détailler notre démarche, 
question par question en présentant les défis rencontrés,
les solutions élaborées et la répartition de notre travail.


## Question 1 :
#### Proposez une implémentation d’un graphe, qui représente une grille hexagonale et qui possède toutes les propriétés d’un graphe

*Question réalisée par Alexandre et Margot*

Dans un premier temps, nous avons repris le [code](https://web.isen-ouest.fr/moodle4/pluginfile.php/16213/mod_resource/content/0/hexgrid_viewer.py) fournit sur le mooodle. 

Nous avons ensuite découpé ce code en plusieurs fichiers.

Forme.py qui contient :
```python
Class Forme :
```
Cette classe représente une forme avec une couleur et une bordure.

Rect.py et Cercle.py qui contient :
```python
Class Rect :
Class Circle : 
```
Ces classes sont des sous classes de 'Forme',
chacune représentant respectivement un rectangle et un cercle.
Elles sont dotées de la méthode 'get', qui renvoie un objet Matplotlib (Rectangle ou Circle) configuré avec les propriétés de la forme.

HexGridViewier.py qui contient :
```python
Class HexGridViewer :
```
Cette classe nous permet de réaliser l'affichage de la grille hexagonale,
on y retrouve un constructeur '__ init __' qui prend en paramètre la largeur et la hauteur de la grille hexagonal,
les méthodes 'add_color', 'add_alpha', 'add_symbol', et 'add_link' qui permettent d'ajouter des informations à chaque hexagone.
La méthode show génère la visualisation en utilisant Matplotlib, 
avec des options pour personnaliser les couleurs, la transparence, les symboles, les liens, etc.
Les méthodes 'get_color' et 'get_alpha' permettent quant à elle de récupérer les informations associées à un hexagone spécifique.
Pour finir, la méthode get_neighbours.
C'est cette fonction qui nous permet de retourner les coordonnées des hexagones voisins d'un hexagone donné.
Cette fonction nous sera utile dans les futures questions.

Nous avons ensuite utilisé et réadapté les fonctions réaliser lors des TP du jeudi matin afin d'implémenter un graphe.
Comme nous avions à peu près le même code, cela a été plus simple.
On a ainsi ajouté deux fichiers.
Ces fichiers définissent des classes pour représenter des graphes, en particulier des graphes dirigés ou non dirigés avec une représentation sous forme de liste d'adjacence.
On retrouve comme premier fichier Graph.py, 
qui contient la classe abstraite :
```python
Class Graph :
```
Cette classe propose des méthodes abstraites pour ajouter des sommets, des arêtes, vérifier l'existence d'une arête, obtenir des informations sur les voisins, et d'autres opérations de base. 
Les sous-classes de cette classe doivent implémenter ces méthodes pour créer des graphes spécifiques.


C'est exactement ce que fait le fichier Graph_List.py, contenant la classe : 
```python
Class GraphList :
```
Cette classe hérite de la classe abstraite 'Graph' et implémente des méthodes comme l'ajout de sommet et d'arêtes, la vérification de l'existence d'une arête, l'obtention de la liste des sommets, des labels, etc.

Tous ces fichiers sont ensuite utilisés dans la main.py pour créer un programme qui génère une grille héxagonale. 
Il intègre les classes GraphList et HexGridViewer pour créer et afficher une grille hexagonale basée sur un graphe aléatoire.

## Question 2 :
#### Proposez une extension de cette implémentation, permettant :
#### — de labeliser les sommets par un type de terrain de votre choix (herbe, montagne, route, eau, etc...) ;
#### — de labeliser les sommets par une altitude.

*Réalisation de la classe Vertex par margot*
*Modification des fonctions de la classe Graph_List réalisé par alexandre et Margot*
*Modification de la fonction show du fichier HexGridViewer.py réalisé par Alexandre*
*Modification du paramètre alias dans le fichier question.py lors de l'appel de la fonction réalisé par Alexandre et margot*

Afin de réaliser cette extension, nous avons creer un fichier vertex.py.
contenant la classe :
```python
Class Vertex :
```
Cette classe représente un sommet dans un graphe. Chaque sommet est caractérisé par ses coordonnées (coord), un type de terrain (terrain), et une altitude (alt).
La méthode '__ init __' initialise les attributs du sommet lors de sa création.

Nous avons ensuite modifié les paramètres de nos fonctions dans Graph_List.
Une modification a été apportée au fichier HexGridViewer.py notamment dans la fonction show.
Un paramètre show_altitude a été rajouté.
Il permet lorsque le paramètre debug_coords est faux,
d'afficher l'altitude de chacun de nos sommets.
Chaque altitude étant initialisée dans le fichier question.py par :
```python
alt = random.uniform(0.2, 1)
```
Nous avons décidé d'afficher simplement chacune de nos altitudes en multipliant alpha(l'altitude) par 10 et la transformée en int.
Voici la modification apportée :
```python
 # Ajoute du texte à l'hexagone soit les coordonnées
                if debug_coords:
                    # Ajoute du texte à l'hexagone soit les coordonnées
                    text = f"({row}, {col})"  # Le texte que vous voulez afficher
                    ax.annotate(text, xy=center, ha='center', va='center', fontsize=8, color='black')
                else:
                    if show_altitude:
                        # alpha = altitude of Vertex
                        # *10 to improve the visibility of altitude in the graph
                        text_altitude = f"{int(self.__alpha[(row, col)] * 10)}"
                        #text_altitude = f"{float(self.__alpha[(row, col)] )}"
                        ax.annotate(text_altitude, xy=center, ha='center', va='center', fontsize=6, color='black')
```
Enfin, le dernier changement a été effectué dans Le fichier question.py, lors de l'appel de la fonction show,
on a apporté des modifications dans l'alias afin de renommer les noms de la légende pour des couleurs spécifiques.
```python
# AFFICHAGE DE LA GRILLE
    # alias permet de renommer les noms de la légende pour des couleurs spécifiques.
    # debug_coords permet de modifier l'affichage des coordonnées sur les cases.
    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=True, debug_coords=False)
```


## Question 3:

*Réalisé par Margot et Alexandre*

Les tests de programme sont réalisés dans le fichier questions.py.
Dans ce fichier, on retrouve les différentes fonctions répondant à chacune des questions et qui seront par la suite appelées dans le main.
La fonction répondant aux trois premières question est :
````python
def first_part(hex_grid: HexGridViewer):
    """
    Function to anser to the question 1, 2, 3
    :param hex_grid:
    :return:
    """
````
Cette fonction reprend le travail qui a été effectué dans les questions 1, 2.
Le but est d'afficher une grille qui possède un terrain aléatoire et des altitudes aléatoires.

Pour ce faire on crée dans un premier temps un graphe.
N'ayant pas besoin d'être orienté, on l'initialise à false.
On parcourt en largeur et en profondeur notre grille 
Et on fait prendre à chaque coordonnée ({row}, {col}) une couleur aléatoire et une altitude aléatoire entre 0.2 et 1.
Ces étapes effectuées, on ajoute ce sommet à notre graphe.
````python
# CREATION D'UN GRAPHE
    graphe_grid = GraphList(False)
    for i in range(0, hex_grid.get_width()):
        for j in range(0, hex_grid.get_height()):
            t = random.choice(graphe_grid.dict_elem)
            alt = random.uniform(0.2, 1)
            graphe_grid.add_vertex((i, j), t, alt)
````
Reste maintenant l'ajout d'arête à nos sommets.
Pour ce faire, on parcourt l'ensemble des sommets de notre graphe et pour chaque voisin de notre sommet, on ajoute une arête.

````python
for v in graphe_grid.vertex():
        # ADD EDGES BETWEEN VERTEX
        list = graphe_grid.get_neighbour(v)
        for v2 in list:
            graphe_grid.add_edge(v, v2)
````
Enfin, on rajoute les couleurs, l'altitude en appelant les fonctions add_color() et add_alpha() de la classe HexGridViewer
prenant en paramètre, nos sommets : v(coord, terrain, alt).
Et on appelle la fonction show afin de pouvoir afficher notre graphe sous forme de grille.

````python
        # MODIFICATION DE LA COULEUR D'UNE CASE
        hex_grid.add_color(v)
        hex_grid.add_alpha(v)

    # AFFICHAGE DE LA GRILLE
    # alias permet de renommer les noms de la légende pour des couleurs spécifiques.
    # debug_coords permet de modifier l'affichage des coordonnées sur les cases.
    hex_grid.show(
        alias={"royalblue": "water", "chocolate": "path", "forestgreen": "grass", "grey": "stone", "snow": "snow",
               "red": "fire", "black": "obsidian"}, show_altitude=True, debug_coords=False)

````

## Question 4:
*Réalisé par Alexandre*

Afin de répondre à cette question, a été implémenté dans le fichier Graph_List.py une fonction def zone.

Le but de cette fonction est en partant d'un sommet et d'une distance particulière qui définira la taille de la zone en vertex,
de générer une zone régulière s'étendant sur la carte. 
Tels que le montre l'image ci-dessous :

![img_3.png](img_3.png)

Dans notre fonction, nous prenons en paramètre le graphe sur lequel nous opérons, 
le point de départ de notre zone, la distance souhaitée pour notre zone, ainsi qu'un dictionnaire. 
Ce dictionnaire permet de changer la couleur chaque fois que la distance augmente de 1.

Le concept derrière cette fonction est d'initialiser le centre de notre zone avec le sommet spécifié en paramètre, ainsi que sa position dans la zone, initialement à 0.
Ensuite, nous progressons en vérifiant que notre liste n'est pas vide et que nous n'avons pas atteint la limite de distance spécifiée. 
À chaque itération, nous retirons le premier élément de notre liste et examinons les voisins autour de ce sommet. Si le voisin n'a pas été visité, nous l'ajoutons à notre liste en augmentant sa distance actuelle de 1. 
Dès que la division de cette distance actuelle par 6 donne un résultat de 0, nous modifions la couleur de notre liste.
````python
    def zone(self, centre: Vertex, dist, dico: dict):
        """
        Get the area around a vertex
        :type centre: the center vertex
        :param dist: dist of the area
        :param dico: the dictionary of the corresponding area
        :return: zone of neighbor
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
````
Un objet zone de cette fonction sera ensuite créer pour gérer plus facilement les différents types de zone présents dans notre graphe et utiliser à l'avenir. 

La fonction zone sera ensuite appelée dans le fichier question.py.
Cela va permettre d'afficher notre zone.
En partant d'un graph, on mettra sur l'ensemble de notre terrain de la neige afin de mieux voir la zone.

Pour observer la grille, il suffira d'aller dans le fichier main.py et de dé commenter question_zone.

## Question 5:
*Réalisé en majeure partie par Alexandre, mais aidé par margot*

Cette question s'est divisée en 2 temps.
Dans un premier temps, il a fallu créer une méthode permettant de trouver le sommet le plus haut de notre carte.

Pour ce faire, nous avons décidé d'implémenter dans le fichier Graph_List.py une fonction find_higher qui renvoie le sommet le plus haut sur une liste de sommet passer en paramètre (dans notre cas graph_grid.vertex).
Or il arrive d'obtenir plusieurs sommets de la même altitude.
Dans ce cas, on va utiliser la fonction find_ListOfhigher.
Cette fonction complète la fonction precedente et renvoie après avoir recherché via find_higher le sommet le plus haut,
une liste contenant tous les vertex ayant la même altitude maximale que le premier vertex trouvé.

Ces 2 méthodes implémentées, nous avons décidé d'utiliser l'algorithme DFS afin de tracer des rivières à partir d'un point donné sur la carte.
Nous l'avons quelque peu boosté afin qu'il nous renvoie le chemin le plus long possible.

Cette méthode a également été implémenté dans le fichier Graph_List.py.
Nous recherchons les points les plus hauts de la grille à l'aide de la fonction find_higher et find_ListOfhigher puis
à l'aide d'un code DFS nous cherchons le chemin le plus longs via l'exploration récursive des voisins ayant une altitude inférieure ou égale à celle de départ.

En découlera de DFS, la fonction Rivière qui prend en paramètre le point le plus haut et détermine le chemin le plus long.
Une autre méthode sera aussi créer, "rivières" qui prendra une liste de vertex en paramètre et déterminera le chemin le plus long pour chacun des sommets choisis en paramètre.

Cette question sera appelée de la même manière que la question précédente. 
La fonction riviere sera appelée dans le fichier question.py.
Cela va permettre d'afficher notre riviere.
En partant d'un graph, on mettra sur l'ensemble de notre terrain de la neige afin de mieux voir la rivière.

Pour observer la grille, il suffira d'aller dans le fichier main.py et de dé commenter question_river(hex_grid).


## Qustion 6:
*Réaliser par Alexandre et Margot,*
*Axe d'amélioration réalisée par Alexandre*

Cette question propose un algorithme, qui, s’inspirant des deux precedents, génère une
carte aléatoirement, de sorte que les altitudes soient "logiques" et que les types de terrains
aient une cohérence, avec les rivières.

Pour ce faire, nous avons dans un premier temps, repris la méthode zone effectuer par Alexandre dans une méthode nommé Zone 2.
Cette méthode va concrètement reprendre zone, mais en fonction du type de zone, définir une altitude à prendre en compte.
Pour une foret, on va par exemple retrouver une altitude qui varie entre 0.3 et 0.6 tandis que pour une montagne, on va retrouver une altitude qui varient entre 0.8 et 1.
Lors du parcours des voisins afin de savoir s'il sont visité ou non, on va selon les zones 


````python
    def zone2(self, centre: Vertex, dist, typeZone, dico: dict):
        """
        Get the area around a vertex
        :type centre: the center vertex
        :param dist: dist of the area
        :param dico: the dictionary of the corresponding area
        :return: zone of neighbors
       """
        queue = [(centre, 0)]
        zone = Zone(centre, dist, typeZone, dico)
        current_distance = 0
        visited = set()
        visited.add(centre)

        while queue:
            current_vertex, current_distance = queue.pop(0)  # queue.pop(0)
            current_vertex.terrain = zone.areaDicoType[current_distance % 4]
            # calcul altitude
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
````

Pour ajouter de la logique à notre carte, nous avons créé des zones ayant des altitudes dans un intervalle défini qui varie
faiblement d'un voisin à l'autre que nous ajoutons sur notre carte qui à également des sommets d'altitudes aléatoire
Ces altitudes varient d'une valeur comprise dans un intervalle compris entre 0 et 0,2.

Proposez maintenant un algorithme, qui, s’inspirant des deux prédécedents, génère une
carte aléatoirement, de sorte à ce que les altitudes soient "logiques" et que les types de terrains
aient une cohérence, avec des rivières.
Extension bonus : l’eau peut ne pas être une rivière, par exemple, avec les lacs. Quelle contrainte
cela ajoute au programme ? Comment faire ?


## Question 7 :
*Réaliser par Margot*
Pour trouver le chemin le plus rapide entre 2 villes, nous utilisons la fonction pcc qui determine le plus court chemin 
entre deux sommets quand nous n'avons pas de contraintes de pondération.
Il s'agit d'un algorithme ayant une complexité temporelle en O(|S|+|A|) avec S le nombre de sommets du graphe et A le nombre
d'arêtes.

Voici le tableau avec la compexité temporelle en fonction du nombre de villes et de la taille de la grille :

![img_1.png](img_1.png)

## Question 8:
*Réalisé en majeure partie par Margot, mais aidé par alexandre*
Maintenant, nous pouvons pondérer les arêtes en fonction du type de terrain. Pour se faire nous prenons le poids du type
de terrain d'arrivée, prédéfini dans le dictionnaire :
```python
dict_dist = { 'gray' : 1, 'darkolivegreen':1, 'sandybrown' : 2, 'forestgreen' : 2, 'darkgreen' : 2, 'sienna':3, 'black': 2,
              'snow':4, 'darkred':4, 'saddlebrown': 3, 'green': 1, 'royalblue': 50, 'red': 50, 'turquoise': 50}
``` 
À cette valeur, nous ajoutons la différence d'altitude entre les deux sommets pour obtenir des poids propres à chaque arête.
Pour empecher les chemins de passer par les rivières, il faut supprimer les arrêtes des sommets par lesquels passent une rivière
ou une zone aquatique. Il faut également empêcher le passage dans la lave en utilisant la même méthode.

Nous utilisons l'alorithme de Dijkstra pour trouver le chemin le plus court entre deux villes en prennant en compte la pondération
de chaque arête.

Voici un tableau pour représenter la complexité temporelle de l'algorithme de Dijkstra en fonction du nombre de villes 
et la taille de la grille :
![img_2.png](img_2.png)

## Question 9:
*Réalisé par Margot*
Pour créer ce réseau, la solution la plus logique pour nous est d'utiliser l'algorithme de Kruskal.
Nous avons rencontré de nombreuses difficultés lors de l'implémentation de cet algorithme dans notre code en le liant avec
la grille et en utilisant la classe vertex qui contient toutes les informations sur un sommet.

Nous avons dans un premier temps eu du mal, car les arrêtés ne s'affichaient pas uniquement avec des sommets voisins mais
avec des sommets d'un côté à l'autre de la carte.
Ensuite le plus gros problème que nous avons rencontré est le fait que certaines arêtes présentes sur le chemin disparaissaient
nous empêchant de determine le chemin en entier entre deux villes. Ce problème de disparition d'arrêtes est certainement 
lié au fait que nous supprimons les arrêtes passant dans les rivières et que nous n'avions pas encore enlever le fait qu'une
ville puisse apparaitre dans une rivère.

## Question 10:

Étant donné nos difficultés pour implémenter et répondre à la question précédente nous n'avons pas eu le temps de résoudre cette question.
