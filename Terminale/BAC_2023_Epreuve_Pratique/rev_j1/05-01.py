# -*- coding: utf-8 -*-


from random import randint


def lancer(n):
    lst = []
    for i in range(n):
        nb = randint(1, 6)
        lst.append(nb)
    return lst


def lancer_v2(n):
    return [randint(1, 6) for i in range(n)]


def paire_6(tab):
    cpt = 0
    for elt in tab:
        if elt == 6:
            cpt += 1
    return cpt >= 2


assert paire_6([1,2,3,4,5,6]) is False
assert paire_6([6,6,6,6,6,6,6]) is True
           