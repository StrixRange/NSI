# -*-coding : utf-8-*-

## Exercice 1

def test_pytagore(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


## Exercice 2

def valeur_absolue(a):
    if a < 0:
        return -a
    else:
        return a


## Exercice 3

def max2(a, b):
    if a > b:
        return a
    else:
        return b


## Exercice 4

def max3(a, b, c):
    return max2(max2(a, b), c)


## Exercice 5

def puissance(x, k):
    a = 1
    acc = 1
    for i in range(k):
        acc = x**i
        a = a + acc
    return a


## Exercice 6

def bissextile(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)


## Exercice 7

def nbjoursannee(a):
    if bissextile(a) is False:
        return 365
    else:
        return 366


## Exercice 8

def nbjoursmois(a, m):
    if m == 2 and bissextile(a) is True:
        return 29
    elif m == 2:
        return 28
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        return 30


## Exercice 9

def nbjours(jn, mn, an, j, m, a):
    nombre_total_annees = jn - a
    nombre_total_mois =

