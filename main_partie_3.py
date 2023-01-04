
from Graphe import Graphe
from partie_3 import *


if __name__ == '__main__':
    sommet = 10
    graphe = Graphe(sommet)
    dictionnaire = graphe.generer_graphe()
    print("eeeeeeeeeeeeeeeeeeeee")
    print(dictionnaire)
    G = graphe.dessiner_graphe2()
    L = degenerecy(graphe=graphe)
    print(L)
    operator_ss_graphes = generer_sous_graphes(
        graphe=graphe, sommets_pas_traites=list(L), sous_graphes_actu=[], voisins=list(L))

    for ss_graphe in operator_ss_graphes:
        print(ss_graphe)
