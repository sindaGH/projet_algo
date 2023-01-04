from matplotlib import pyplot as plt
from Graphe import Graphe
#from Partie_2 import *

import networkx as nx
if __name__ == '__main__':

    """
    Partie 1 : 1- generation graphe aléatoire 
                    maximum degre
                    histogramme sommet degre 
                    nombre des chemins du longeur 2
                2- implementation base de donnée Stanfold
    """
    # on initialise un graphe de le nombre des sommets donnée en paramètre
    G = Graphe(7)
    G.generer_graphe()
    print("La liste d'adjacence dictionnaire  \n")
    print(G.dictionnaire)
    g = G.dessiner_graphe_aleatoire()
    G.afficher_degre_max(graphe=g)
    G.histogramme_graphe(graphe=g)
    G.nombre_chemein_longeur_2(graphe=g)
    """
    Cette partie de code pour tester les grands bases de Scantfold elle prend en paramètre le nom_du_fichier.txt
    g = dessiner_graphe_facebook(".facebook_combined.txt")
        histogramme_graphe(g)
        degre_max(g)
        plt.show()

    """
    """
    Partie 2 : implémentation algo du bron kerbosch version avec pivot 
    """
    P = nx.nodes(G=g)
    r = []
    x = []
    # liste des cliques maximales du graphe retourner par l'algo de bron_kerbosch
    list = G.bron_kerbosch_avec_pivot(graphe=g, P=P, R=None, X=None)
    print("les cliques maximales dans ce graphes sont : \n ")
    for element in list:
        print(element)
    plt.show()
