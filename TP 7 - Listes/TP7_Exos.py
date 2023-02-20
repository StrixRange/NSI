
## Exercice 1

def occurrences(v, tab):
    cpt = 0
    for i in tab:
        if i == v:
            cpt = cpt + 1
    return cpt


## Exercice 2

def echange(tab, i, j):
    tmp = tab[i]
    tab[i] = tab [j]
    tab[j] = tmp
    return tab


## Exercice 3

def somme(tab):
    return sum(tab)                     # sum = somme des valeurs d'un tableau


# Sans sum

def somme1(tab):
    tot = 0
    for i in tab:
        tot = tot + i
    return tot


def moyenne(tab):
    if sum(tab) != 0:
        caca = sum(tab) / len(tab)      # len = longeur du tableau
        return caca
    else:
        return 0


## Exercice 4

def produit(tab):
    total = 1
    for i in range(0, len(tab)):
        total *= tab[i]
    return(total)


## Exercice 5

def mirroir(tab):
    n = len(tab)
    mid = n // 2
    for i in range(mid):
        echange(tab, i, n-1-i)
    return tab


## Exercice 6

from random import randrange

def tab_entiers(a, b):
    randrange(1, 100)
