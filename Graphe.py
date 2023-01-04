"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%               Outils Pour La Conception D'Algorithmes
%   Auteurs: Gharsi Sinda
             Omezzine Manar
             Ben Sghaier Mohammed Ameur
%   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
"""
        première partie:

"""


import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
dictionnaire = {}


class Graphe:
    def __init__(self, sommet):
        self.sommet = sommet
        self.dictionnaire = dictionnaire
    """
     fonction generer_graphe permettre à gérer le graphe aléatoirement selon la probabilité p
    """

    def generer_graphe(self):

        i = 0
        j = 0
        for i in range(self.sommet):
            self.dictionnaire[i] = list()
            for j in range(self.sommet):
                proba = random.gauss(0, 2)
                if (proba > 0) and (proba < 1):
                    if (int(i) != int(j)):
                        self.dictionnaire[i].append(str(j))
     #   return self.dictionnaire

    """
     fonction dessiner_graphe permettre de dessiner le graphe selon les valeurs de  
     son dictionnaire correspondant en utlisant les fonctions prédéfini de la bibliothèque nx de networkX

    """

    def dessiner_graphe_aleatoire(self):
        G = nx.Graph()
        for keys in self.dictionnaire.keys():
            G.add_node(int(keys))

        for keys, valuues in self.dictionnaire.items():
            for value in valuues:
                #print(keys, value)
                G.add_edge(int(keys), int(value))

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color="lavender", node_size=800)
        # fonction prédéfinie pour les étiquettes des nœuds sur le graphe G
        nx.draw_networkx_edges(G, pos, arrows=False)
        # fonction prédéfinie pour écrire un titre dans le graphe G
        # fonction prédéfinie pour les noeuds du graphe
        nx.draw_networkx_labels(G, pos)
        # fonction prédéfinie pour dessiner les aretes du graphe G
        plt.title("la Génération d'un graphe aléatoire")

        return G
        # fonction prédéfinie pour afficher le graphe

    """
     fonction  afficher_degre_max  permettre de retourner  la valeur de plus haut degré du graphe 

    """

    def afficher_degre_max(self, graphe):
        liste_degree = sorted((d for n, d in graphe.degree()), reverse=True)
        dmax = max(liste_degree)
        print("Le degré maximum du graphe est : " + str(dmax))
        return(dmax)
    """
     fonction histogramme_graphe permettre de dessiner la valeur de plus haut degré du graphe 
    
    """

    def histogramme_graphe(self, graphe):
        '''

        '''
        # liste de qui retourne une liste de : (sommet, degre de sommet)
        degre_graphe = graphe.degree()
        print(degre_graphe)
        # liste de qui filtre la liste de degre_graphe pour retourner la liste de degre
        liste_de_degre = sorted((d for n, d in degre_graphe), reverse=True)
        print(liste_de_degre)

        fig = plt.figure("histogramme du graphe aléatoire ", figsize=(5, 5))
        axe = fig.add_subplot()
        # cette fontion nous permettre de créer les deux axes x ,y on fonction de degré et la nbre
        # des sommets ayant ce degré a partir de la liste_de_degre
        axe.bar(*np.unique(liste_de_degre, return_counts=True))
        axe.set_title("histogramme de degré -- nombre sommet")
        axe.set_xlabel("Degré")
        axe.set_ylabel("nombre des sommets ")
        fig.tight_layout()
        # plt.show()
    """
     fonction nombre_chemein_longeur_2 permettre de trouver le nbre des chemins de longeur deux  
    
    """

    def nombre_chemein_longeur_2(self, graphe):
        #matrice = nx.adjacency_matrix(graphe)
        #matrice_adjacence_au_carrée = matrice*matrice
        matrice_adjacence = nx.to_numpy_matrix(graphe)
        #matrice_ad = np.matrix(matrice_adjacence)
       # print(matrice_ad)
        print("matrice d'adjacnece du graphe :")
        print(matrice_adjacence)
        matrice_adjacence_au_carrée = matrice_adjacence*matrice_adjacence
        print("matrice d'adjacnece au carre du graphe :")
        print(matrice_adjacence_au_carrée)
        diagonale_matrice = matrice_adjacence_au_carrée.diagonal()
        #diagonale = matrice_adjacence.diagonal()
        print("diagnole du matrice  :")
        print(diagonale_matrice)
        somme_matrice_carre = np.sum(matrice_adjacence_au_carrée)
        somme_diagonale_carre = np.sum(diagonale_matrice)
        """
        cette boucle pour ne pas compter le nombre de chaemins ayant une arrete entre 
        les deux sommets 

        """
        for i in range(int((self.sommet))):
            for j in range(self.sommet):
                if matrice_adjacence[i, j] == 1:
                    somme_matrice_carre = somme_matrice_carre - \
                        matrice_adjacence_au_carrée[i, j]
        #somme_matrice = np.sum(matrice_adjacence)

        #somme_diagonle_matrice = np.sum(diagonale)
        somme = ((somme_matrice_carre-somme_diagonale_carre
                  )/2)
        print("nombre des chemins du longeur 2 est : "+str(somme))

    """
            deuxième  partie  : implémentation d'algo bron_kerbosch_avec_pivot
                    
    """

    def bron_kerbosch_avec_pivot(self, graphe,  P, R, X):

        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        if len(P + X) == 0:
            yield R
        else:
            # choisir un pivot selon l'algo de Tomita

            pivot = self.pivot_tomita(graphe, P, X)

            # parcourir la liste P privée de N(pivot)
            # avec N(pivot) : la liste des voisins du sommet pivot
            for sommet in list(set(P).difference(nx.neighbors(graphe, pivot))):
                yield from self.bron_kerbosch_avec_pivot(graphe, list(set(P) & set(nx.neighbors(graphe, sommet))), R + [sommet],
                                                         list(set(X) & set(nx.neighbors(graphe, sommet))))

                P.remove(sommet)
                X.append(sommet)

    # choisir un pivot pour minimiser le nombre d'appels récursif
    # cet algorithme consiste à prendre u tel que |P inter N(u)| soit maximal
    # N(u) : les voisins du sommet u.

    def pivot_tomita(self, graphe, P, X):
        #print("algo tomita")
        # L'union de P et X
        P_and_X = list(P + X)
        # initialiser u comme le premier sommet de P union X
        u = P_and_X[0]

        # L'intersection de P et N(u)
        P_inter_voisin_de_u = list(set(P) & set(nx.neighbors(graphe, u)))
        # initialiser le degre max à la taille de la liste ( P inter N(u) )
        degre_max = len(P_inter_voisin_de_u)

        # P Union X privée de u
        # P union X \ {u}
        P_and_X_privee_de_sommet = list(set(P_and_X) - {u})

        for v in P_and_X_privee_de_sommet:
            # L'intersection de P et N(v)
            P_inter_voisin_de_v = list(set(P) & set(nx.neighbors(graphe, v)))
            if len(P_inter_voisin_de_v) > degre_max:
                u = v
                degre_max = len(P_inter_voisin_de_v)
        return u
