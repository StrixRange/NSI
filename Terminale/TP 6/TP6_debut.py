# -*-coding: utf-8-*-


class Cell:

    def __init__(self, val, c=None):
        self.value = val
        self.next = c


def listeN(n, k=1):
    if k > n:
        return None
    else:
        return Cell(k, listeN(n, k+1))


def listeN_v2(n, lsc=None):
    if n == 0:
        return lsc
    else:
        return listeN_v2(n-1, Cell(n, lsc))


def affichage(lsc):
    if lsc is None:
        print("None")
    else:
        print(lsc.value, end=" -> ")
        affichage(lsc.next)