# Créé par nisars, le 04/10/2022 en Python 3.7

# Exercice 1

class Cell:

    def __init__(self, v, c = None):
        self.value = v
        self.next = c

def listeN(n):
    if n == 0:
        return []
    lst = None
    for i in range(n, 0 ,-1):
        c = Cell(i, lst)
        lst = c
    return lst

def affichage_liste(lst):
    c = lst
    while c is not None:
        print(c.value, end=" -> ")
        c = c.next

def occurences(x, lst):
    w = 0
    c = lst
    while c is not None:
        if x is c.value:
            w = w + 1
        c = c.next
    return w

def occurencesnul(x, lst):
    w = 0
    for i in range(len(lst)):
        if x == lst[i]:
            w += 1
    return w

def trouvenul(x, lst):
    b = False
    for i in range(len(lst)):
        if x == lst[i]:
            b = True
            return i
    if b is False:
        return None

def trouve(x, lst):
    g = 0
    c = lst
    while c is not None:
        if x is c.value:
            return g
        c = c.next
        g += 1
    return None

def identiques(l1, l2):
    c = l1
    d = l2
    bool = False
    while c is not None and d is not None:
        if c.value == d.value:
            bool = True
            c = c.next
            d = d.next
        else:
            return False
    if bool is True:
        return True


def inserer(x, lst):
    c = lst
    lst2 = None
    while c is not None:
        if c.value < x:
            lst2 = c
            print("test")
            c = c.next
        if c.value > x:
            print("ça a marché lets gooooooooooo")


def liste_de_tableau(t):
    pass


def derniere_cellule(lst):
    c = lst
    cpt = 0
    while c is not None:
        cpt += 1
        c = c.next
    return cpt






