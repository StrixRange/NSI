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


def occurences(x, lsc):
    if lsc is None:
        return 0
    elif lsc.value == x:
        return 1 + occurences(x, lsc.next)
    else:
        return occurences(x, lsc.next)


def trouve(x, lsc, k=0):
    if lsc is None:
        return None
    elif lsc.value == x:
        return k
    else:
        return trouve(x, lsc.next, k+1)


def identiques(l1, l2):
    if l1 is None and l2 is None:
        return True
    elif l1 is None or l2 is None or l1.value != l2.value:
        return False
    else:
        return identiques(l1.next, l2.next)


def identiques_v2(l1, l2):
    if l1 is None:
        return l2 is None
    if l2 is None:
        return l1 is None
    return l1.value == l2.value and identiques_v2(l1.next, l2.next)


def inserer(x, lsc):
    if lsc is None:
        return Cell(x, lsc)
    elif lsc.value <= x:
        return Cell(lsc.value, inserer(x, lsc.next))
    else:
        return Cell(x, lsc)


def liste_de_tableau(t):
    if t == []:
        return None
    else:
        return Cell(t[0], liste_de_tableau(t[1:]))


def concatener(l1, l2):
    if l1 is not None:
        return Cell(l1.value, concatener(l1.next, l2))
    elif l2 is not None:
        return Cell(l2.value, l2.next)
    else:
        return None


def concatener_light(l1, l2):
    if l1 is None:
        return l2
    else:
        return Cell(l1.value, concatener_light(l1.next, l2))


def longueur(lsc):
    if lsc is None:
        return 0
    else:
        return 1 + longueur(lsc.next)


def nth_element(n, lsc):
    if lsc is None:
        raise IndexError('invalid index')
    elif n == 0:
        return lsc.value
    else:
        return nth_element(n-1, lsc.next)
