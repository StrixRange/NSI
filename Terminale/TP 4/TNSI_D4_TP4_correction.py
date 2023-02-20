class Cell:

    def __init__(self, v, c):
        self.value = v
        self.next = c


lsc = Cell(1, Cell(2, Cell(3, None)))


def listeN(n):
    lst = None
    for i in range(n, 0, -1):
        c = Cell(i, lst)
        lst = c
    return lst


def affiche_liste(lst):
    c = lst
    while c is not None:
        print(c.value, end=' -> ')
        c = c.next


def occurences(x, lst):
    cpt = 0
    c = lst
    while c is not None:
        if c.value == x:
            cpt += 1
        c = c.next
    return cpt


def trouve(x ,lst):
    rang = 0
    c = lst
    while c is not None:
        if c.value == x:
            return rang
        else:
            rang += 1
            c = c.next
    return None


def identiques(l1, l2):
    c1 = l1
    c2 = l2
    while c1 is not None and c2 is not None:
        if c1.value == c2.value:
            c1 = c1.next
            c2 = c2.next
        else:
            return False
    return c1 is None and c2 is None


# Correction du prof, mais c'est faux. Renvoie juste comme si la liste t était [0,1,2,n...] = 0 -> 1 -> 2 -> n /// Voir ma correction ci dessous

# def liste_tableau(t):
#     lst = None
#     n = len(t)
#     for i in range(n-1, -1, -1):
#         c = Cell(i, lst)
#         lst = c
#     return lst

def liste_tableau(t):
    lst = None
    n = len(t)
    for i in range(n-1, -1, -1):
        c = Cell(t[i], lst)
        lst = c
    return lst

def liste_tableau_v2(t):
    lst = None
    for elt in reversed(t):
        lst = Cell(elt, lst)
    return lst


def derniere_cellule(lst):
    c = lst
    while c is not None:
        save = c.value
        c = c.next
    return save


def renverser(lst):
    c = lst
    lst2 = None
    while c is not None:
        lst2 = Cell(c.value, lst2)
        c = c.next
    return lst2


def concatener(l1, l2):
    lst = None
    c = l1
    while c is not None:
        lst = Cell(c.value, lst)
        c = c.next
    c = l2
    while c is not None:
        lst = Cell(c.value, lst)
        c = c.next
    return renverser(lst)


def concatener_v2_lavergne(l1, l2):
    lst = None
    for c in (l1,l2):
        while c is not None:
            lst = Cell(c.value, lst)
            c = c.next
    return renverser(lst)






















