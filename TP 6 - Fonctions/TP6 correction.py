# Créé par se4install, le 10/12/2021 en Python 3.7

def test_Pythagore(a, b, c):
    return a**2 + b**2 == c**2

def valeur_absolue(x):
    if x >= 0:
        return x
    else:
        return -x


def valeur_absolue_v2(x):
    return x if x >= 0 else -x

def max2(a, b):
    return a if a > b else b

def max3(a, b, c):
    return max2(max2(a, b), c)

def puissance(x, k):
    resultat = 1
    for i in range(k):
        resultat = resultat * 2
    return resultat

def bissextile(a):
    return (a % 4 == 0 and a % 100 != 0) or a % 400 == 0

def nbjoursannee(a):
    if bissextile(a) is True:
        return 366
    else:
        return 365

def nbjoursannee_v2(a):
    return 366 if bissextile(a) else 365


def nbjoursmois(a, m):
    if m == 2 and bissextile(a) is True:
        return 29
    elif m == 2:
        return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31


def nbjours(jn, mn, an, j, m, a):
    acc = 0
    for i in range(an+1, a):
        acc = acc + nbjoursannee(i)

    for i in range(mn, 13):
        acc = acc + nbjoursmois(an, i)
    acc = acc - jn

    for i in range(1, m):
        acc = acc + nbjoursmois(a, i)
    acc = acc + j

    return acc






