# Devoir maison graphe

## Introduction :

Au sein de notre parcours en ingénierie à l'ISEN de Caen,
nous avons dû effectuer un devoir maison en théorie.
Notre tâche consistait à modéliser une zone géographique en deux dimensions,
exploitant un code source initial fourni par notre professeur.
L'utilisation de la bibliothèque Python, Matplotlib et Pyplot, a facilité la représentation visuelle de notre modèle.

La structure des TP que nous avions réalisé en cours
nous a permis de répondre plus facilement aux questions demandées.
Afin de faciliter la communication et le travail d'équipe,
nous avons opté pour l'utilisation de Github.
Cette plateforme nous a permis de suivre les contributions individuelles de chacun lorsque nous n'étions pas ensemble.
Nous avons aussi utilisé discord lorsque l'on était tous les deux disponible et quand nous avions des problèmes sur une fonction,
l'utilisation de code together nous a permis de travailler ensemble.

Ce rapport a pour objectif de détailler notre démarche, 
question par question en présentant les défis rencontrés,
les solutions élaborées et la répartition de notre travail.


## Question 1 :
#### Proposez une implémentation d’un graphe, qui représente une grille hexagonale et qui possède toutes les propriétés d’un graphe

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
Cette classe est la plus principale,
c'est elle qui permet l'affichage de la grille hexagonale
on y retrouve un constructeur '__ init __' qui prend en paramètre la largeur et la hauteur de la grille hexagonal,
les méthodes 'add_color', 'add_alpha', 'add_symbol', et 'add_link' qui permettent d'ajouter des informations à chaque hexagone.
La méthode show qui génère la visualisation en utilisant Matplotlib, 
avec des options pour personnaliser les couleurs, la transparence, les symboles, les liens, etc.
Les méthodes 'get_color' et 'get_alpha' permettent quant à elle de récupérer les informations associées à un hexagone spécifique.
Pour finir, la méthode get_neighbours,
c'est elle qui nous permet de retourner les coordonnées des hexagones voisins d'un hexagone donné.
Cette fonction nous sera utile dans les futures questions.

Nous avons ensuite utilisé les fonctions réaliser lors des TP du jeudi matin afin d'implémenter un graphe.
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


C'est exactement ce que fait le fichier Graph_List.py, contenant la classe 'GraphList'.
Cette classe hérite de la classe abstraite 'Graph' et implémente des méthodes comme l'ajout de sommet et d'arêtes, la vérification de l'existence d'une arête, l'obtention de la liste des sommets, des labels, etc.

Tous ces fichiers sont ensuite utilisés dans la main.py pour créer un programme qui génère une grille héxagonale. 
Il intègre les classes GraphList et HexGridViewer pour créer et afficher une grille hexagonale basée sur un graphe aléatoire.

## Question 2 :
#### Proposez une extension de cette implémentation, permettant :
#### — de labeliser les sommets par un type de terrain de votre choix (herbe, montagne, route, eau, etc...) ;
#### — de labeliser les sommets par une altitude.


