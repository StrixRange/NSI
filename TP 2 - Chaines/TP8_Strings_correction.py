# -*-coding: utf-8-*-

def longueur(st):
    cpt = 0
    for lettre in st:
        cpt = cpt + 1
    return cpt


def compte_les_e(st):
    cpt = 0
    for lettre in st:
        if lettre == 'e':
            cpt = cpt + 1
    return cpt


def occurence(char, st):
    cpt = 0
    for lettre in st:
        if lettre == char:
            cpt = cpt + 1
    return cpt


def appartenance_v1(char, st):
    trouve = False
    for lettre in st:
        if lettre == char:
            trouve = True
    return trouve


def trouve(char, st):
    n = len(st)
    for i in range(n):
        if st[i] == char:
            return i
    return -1


def inverse_v1(st):
    res = ''
    for lettre in st:
        res = lettre + res
    return res


def palindrome(st):
    return st == inverse_v1(st)


def inutile(st):
    res = ''
    n = len(st)
    for i in range(n-1):
        res = res + st[i] + '*'
    return res + st[n-1]


def insere(char, ind, st):
    res = ''
    n = len(st)
    for i in range(n):
        if i != ind:
            res = res + st[i]
        else:
            res = res + char + st[i]
    return res


def suppression(char, st):
    res = ''
    for lettre in st:
        if lettre != char:
            res = res + lettre
    return res


def retire(ind, st):
    res = ''
    for i in range(len(st)):
        if i != ind:
            res = res + st[i]
    return res


def tranchage(st, deb, fin):
    res = ''
    for i in range(deb, fin):
        res = res + st[i]
    return res