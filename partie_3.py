
def degenerecy(graphe):
    # Initialisation d'une liste L qui sera retournée
    L = []
    # Initialisation d'une liste D qui contiendra dans chacune
    # de ses cases, les sommets ayant un degré correspondant
    # à l'indiceice de la case
    D = []
    nbr_voisins_max = graphe.afficher_max()
    D = [list() for i in range(nbr_voisins_max + 1)]
    for sommet, liste in graphe.dictionnaire.items():
        i = len(liste)
        D[i].append(sommet)

    k = 0
    n = len(graphe.dictionnaire.keys())
    x = 0

    # while x <= n:
    #   x = x + 1
    # On parcourt les cases de D en cherchant une qui n'est pas vide
    for i in range(nbr_voisins_max + 1):
        j = 0
        if len(D[i]) >= 0:
            # on parcours tous les sommets du degre i on commencant par les sommetes ayant le plus petit degré
            while j < len(D[i]):
                sommet = D[i][j]
                # On ajoute le sommet au début de la liste L
                L.append(sommet)
               # print(L)
                # On supprime ce sommet  de D
                D[i].remove(sommet)
                voisins_j = graphe.dictionnaire[sommet]
                # On parcourt tous les voisins de le sommet correspondant
                # pour chercher tous les  sommets adjacents a ce sommet et mettre leur degré a leur degré-1
                for w in voisins_j:
                    if w not in L:
                        # On cherche à retirer un degré à w et à le déplacer
                        # à l'indice correspondant dans D
                        iterateur = filter(
                            lambda x: x not in L or x == sommet, graphe.dictionnaire[int(w)])
                        list_voisins = list(iterateur)
                        indice = len(list_voisins)
                        if indice > 0:
                            if w in D[indice]:
                                D[indice].remove(w)
                                D[indice - 1].append(int(w))
            j = j+1
       # return L
    # print(L)
    return L
# Cette fonction permet de générer récursivement tous les sous-graphes d'un graphe


def generer_sous_graphes(graphe,  sommets_pas_traites, sous_graphes_actu, voisins):
    # On cherche à récupérer une liste de sommets candidats
    # qu'on va traiter pour décider les intégrer à notre liste de sous-graphes
    if not sous_graphes_actu:
        sommets_candidats = sommets_pas_traites  # L
    else:
        sommets_candidats = list(set(sommets_pas_traites) & set(voisins))
    if not sommets_candidats:
        # On retourne les sous-graphes lorsqu'il n'y a plus de sommets candidats
        yield sous_graphes_actu
    else:
        v = sommets_candidats[0]
        print(v)
        sommets_pas_traites.remove(v)
        yield from generer_sous_graphes(graphe, sommets_pas_traites, sous_graphes_actu, voisins)
        sous_graphes_actu.append(v)
        voisins.extend(graphe.dictionnaire[v])
        yield from generer_sous_graphes(graphe, sommets_pas_traites, sous_graphes_actu, voisins)
