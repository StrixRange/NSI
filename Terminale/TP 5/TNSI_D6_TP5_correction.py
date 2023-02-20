#! /usr/bin/python3
# -*-coding: utf-8-*-

import turtle as tt

# Exercice 1


def compte_a_rebours(n):
    if n == 0:
        print(n)
    else:
        print(n, end=" -> ")
        compte_a_rebours(n - 1)


# Exercice 2


def boucle(i, k):
    if i <= k:
        print(i, end=" ")
        boucle(i + 1, k)


# Exercice 3


def pgcd_recur(a, b):
    if a % b == 0:
        return b
    else:
        return pgcd_recur(b, a % b)


# Exercice 4


def inverse(st):
    if st == "":
        return st
    else:
        return inverse(st[1:]) + st[0]


def inverse_v2(st):
    if st == "":
        return st
    else:
        return st[-1] + inverse(st[:-1])


def inverse_term(st, acc=""):
    if st == "":
        return acc
    return inverse_term(st[1:], st[0]+acc)


# Exercice 5


def somme(t):
    if len(t) == 0:
        return 0
    else:
        return t[0] + somme(t[1:])


def somme_term(t, acc=0):
    if len(t) == 0:
        return acc
    return somme_term(t[1:], acc + t[0])


# Exercice 6


def appartient(v, t, i):
    if i >= len(t):
        return False
    elif t[i] == v:
        return True
    else:
        return appartient(v, t, i + 1)


def appartient_v2(v, t, i):
    if i >= len(t):
        return False
    else:
        return t[i] == v or appartient_v2(v, t, i + 1)


# Exercice 7


def expo_rapide(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return expo_rapide(x**2, n // 2)
    else:
        return x * expo_rapide(x**2, n // 2)


def expo_rapide_term(x, n, acc=1):
    if n == 0:
        return acc
    elif n % 2 == 0:
        return expo_rapide_term(x**2, n // 2, acc)
    else:
        return expo_rapide_term(x**2, n // 2, acc * x)


# Exercice 8


def nombre_de_chiffres(n):
    if n < 10:
        return 1
    else:
        return 1 + nombre_de_chiffres(n // 10)


def nombre_de_chiffres_term(n, acc=1):
    if n < 10:
        return acc
    return nombre_de_chiffres_term(n//10, acc+1)


# Exercice 9


def nombre_de_bits_1(n):
    if n < 2:
        return n
    else:
        return n % 2 + nombre_de_bits_1(n // 2)


# Exercice 10


def binaire(r, n):
    """"Renvoie l'écriture binaire de r sur n bits,
    r supposé compris entre -2**(n-1) et 2**(n-1)-1 inclus."""
    if r < 0:
        return binaire(r+2**n, n)
    elif r < 2:
        return str(r)
    else:
        return binaire(r//2, n) + str(r%2)


# Exercice 11


def nettoie(lst, k=0):
    if k < len(lst) - 1:
        if lst[k] == lst[k + 1]:
            del lst[k + 1]
            return nettoie(lst, k)
        else:
            return nettoie(lst, k + 1)



# Exercice 13


def koch(n, dist):
    if n == 1:
        tt.fd(dist)
    else:
        koch(n-1, dist/3)
        tt.left(60)
        koch(n-1, dist/3)
        tt.right(120)
        koch(n-1, dist/3)
        tt.left(60)
        koch(n-1, dist/3)


# tt.speed(0)
# koch(4, 243)
# tt.done()








