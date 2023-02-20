## Exercice 1

def compte_a_rebours(n):
    if n == 0:
        print(0)
    else:
        print(n, end = " -> ")
        compte_a_rebours(n-1)

## Exercice 2

def boucle(i,k):
    if i == k:
        print(k)
    else:
        print(i, end = " ")
        boucle(i+1, k)

## Exercice 3

def pgcd(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b

def pgcd_rec(a, b):
    pass

## Exercice 4

def inverse(st):
    if len(st) == 0:
        return st
    else:
        return st[-1] + inverse(st[:-1])

## Exercice 5

def somme(t):
    if t == []:
        return 0
    else:
        return t[0] + somme(t[1:])

## Exercice 6

def appartient(valeur, liste, indice):
    if














