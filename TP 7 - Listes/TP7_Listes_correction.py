# -*-coding: utf-8-*-


from random import randrange


def occurences(v, tab):
    cpt = 0
    for elt in tab:
        if elt == v:
            cpt = cpt + 1
    return cpt


def echange(tab, i, j):
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp


def somme(tab):
    total = 0
    for elt in tab:
        total = total + elt
    return total


def moyenne(tab):
    n = len(tab)
    if n == 0:
        return 0
    else:
        return somme(tab) / n


def moyenne_v2(tab):
    return somme(tab)/len(tab) if len(tab)!=0 else 0


def produit(tab):
    acc = 1
    for elt in tab:
        if elt == 0:
            return 0
        else:
            acc = acc * elt
    return acc


def mirroir(tab):
    n = len(tab)
    for i in range(n//2):
        echange(tab, i, n-1-i)


def tab_entiers():
    tab = []
    for i in range(100):
        tab.append(randrange(1, 1001))
    return tab


def tab_aleatoire(n, a, b):
    tab= []
    for i in range(n):
        tab.append(randrange(a, b+1))
    return tab


def suffixe(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    if n1 > n2:
        return False
    else:
        for i in range(n1):
            if tab1[i] != tab2[n2-n1+i]:
                return False
        return True


def suffixe_v2(tab1, tab2):
    n1, n2 = len(tab1), len(tab2)
    if n1 > n2:
        return False
    else:
        for i in range(-1, -(n1+1), -1):
            if tab1[i] != tab2[i]:
                return False
        return True


def hamming(tab1, tab2):
    cpt = 0
    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            cpt = cpt + 1
    return cpt