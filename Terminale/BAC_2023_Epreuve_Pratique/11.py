# 11

# Exercice 1

def convertir(tab):
    """ tab est un tableau d'entiers, dont les éléments sont 0 ou 1,
    et représentant un entier écrit en binaire.
    Renvoie l'écriture décimale de l'entier positif dont la représentation binaire est donnée par le tableau tab"""

    l = len(tab) - 1
    nb = 0
    for elt in tab:
        if elt == 1:
            nb = nb + 2**l
        l = l-1
    return nb


tab = [1, 1, 1, 0] # 1*2**3 + 1*2**2 + 1*2**1 + 0*2**0
def convertir_ProfVac(tab):
    acc = 0
    dim = len(tab)
    for i in range(dim):
        acc = acc + tab[i] * 2**(dim-1-i)
    return acc



# Exercice 2

# Tri insertion de base
def tri_insertion_base(tab):
    n = len(tab)
    for i in range(1, n):
        cle = tab[i]
        j = i - 1
        while j >= 0 and cle < tab[j]:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = cle


def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j est utilisée pour déterminer où placer la valeur à insérer
        j = i-1
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j]:
            tab[j] = tab[j-1]
            j = j+1
        tab[j] = valeur_insertion
    print(tab)








