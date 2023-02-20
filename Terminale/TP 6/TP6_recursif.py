# TP4 mais récursif = TP6

class Cell:

    def __init__(self, val, c=None):
        self.value = val
        self.next = c

def cell_create(n):
    a = listeN(n)
    affichage(a)
    return a


# Exercice 1
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


# Exercice 2
def affichage(lsc):
    if lsc is None:
        print("None")
    else:
        print(lsc.value, end=" -> ")
        affichage(lsc.next)


# Exercice 3
def occurences_pasrs(x, lst):
    w = 0
    c = lst
    while c is not None:
        if x is c.value:
            w = w + 1
        c = c.next
    return w


def occurences(x, lst, w=0):
    if lst is None:
        return w
    elif x == lst.value:
        return occurences(x, lst.next, w + 1)
    else:
        return occurences(x, lst.next, w)


# Exercice 4
def trouve_pasrs(x, lst):
    g = 0
    c = lst
    while c is not None:
        if x is c.value:
            return g
        c = c.next
        g += 1
    return None

def trouve(x, lst, g = 0):
    if lst is None:
        return None
    elif x == lst.value:
        return g
    else:
        return trouve(x, lst.next, g+1)


# Exercice 5
def identiques_pasrs(l1, l2):
    c = l1
    d = l2
    eq = False
    while c is not None or d is not None:
        if c is None or d is None:
            return False
        if c.value == d.value:
            eq = True
        c = c.next
        d = d.next
    return eq


def identiques(l1, l2):
    if l1 is None and l2 is None:
        return True
    elif l1.value == l2.value:
        return identiques(l1.next, l2.next, True)
    else:
        return False


a = listeN(5)
affichage(a)
b = listeN(4)
affichage(b)



# Exercice 6
def inserer(x, lst):
    c = lst
    lst2 = None
    while c is not None and c.value<x:
        tmp = Cell(c.value, lst2)
        lst2= tmp


def inserer_recur(x, lst):
    if lsc is None:
        return Cell(x, lst)
    elif lst.value <= x:
        return Cell(lst.value,inserer_recur(x, lst.next))
    else:
        return Cell(x, lst)



# Exercice 7
def liste_de_tableau(t):
    t2 = t[::-1] #Inverse le tableau
    lst = None
    for i in t2:
        c = Cell(i,lst)
        lst = c
    return affichage(lst)

def liste_de_tableau_recur(t):
    if t == []:
        return None
    return Cell(t[0], liste_de_tableau_recur(t[1:]))


# Exercice 8
def derniere_cellule(lst):
    if lst.next is None:
        return lst.value
    return derniere_cellule(lst.next)









