# -*- coding: utf-8 -*-


def a_doublon(tab):
    n = len(tab)
    for i in range(n-1):
        if tab[i] == tab[i+1]:
            return True
    return False