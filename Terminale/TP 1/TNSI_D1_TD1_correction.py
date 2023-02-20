#-*-coding: utf-8-*-


def division_euclidienne(a, b):
    """Renvoie le quotient entier q et le reste r
    dans la division euclidienne de a par b, où a et b sont des entiers"""
    pass

##

def puissance(x, n):
    """Renvoie x exposant n où x et n sont deux entiers, n supposé positif"""
    r = 1
    for i in range(n):
        # r contient x exposant i
        r = r * x
    return r

assert puissance(3,2) == 9
assert puissance(2,3) == 8
assert puissance(7,0) == 1
assert puissance(-3,0) == 1
assert puissance(0,7) == 0
assert puissance(-4, 4) == 256
assert puissance(-5, 3) == -125

##


def somme_tab(t):
    """Renvoie la somme des éléments d'un tableau t d'entiers non vide, 0 sinon"""
    s = 0
    for i in range(len(t)):
        # s contient la somme des i premières valeurs de t
        s = s + t[i]
    return s

assert somme_tab([1,2,3]) == 6
assert somme_tab([-3,-4,-5]) == -12
assert somme_tab([2,-3,4,-5,6]) == 4


##


#Version bugguée !!!
def appartient(v, t):
    i = 0
    while i < len(t)-1 and t[i] != v:
        i = i+1
    return i < len(t)


assert appartient(3, [3,4,5]) == True
assert appartient(3, [4,5,6,3]) == True
assert appartient(3, [4,5,3,6,7]) == True
#assert appartient(3, [1,2,5,6]) == False


#Version corrigée
def appartient_corrigee(v, t):
    i = 0
    while i < len(t) and t[i] != v:
        i = i+1
    return i < len(t)


def appartient_v2(v, t):
    for item in t:
        if item == v:
            return True
    return False


def appartient_v3(v, t):
    trouve = False
    for item in t:
        if item == v:
            trouve = True
    return trouve


def appartient_v4(v, t):
    t.append(v)
    i = 0
    while t[i] != v:
        i = i+1
    t.pop()
    return i != len(t)
