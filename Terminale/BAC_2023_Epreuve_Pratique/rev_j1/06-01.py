# -*- coding: utf-8 -*-


def recherche(tab, n):
    ind = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            ind = i
    return ind
        