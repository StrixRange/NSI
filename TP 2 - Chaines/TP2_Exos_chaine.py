# -*- coding : utf-8 -*-

# où st = chaîne de caractère

## Exercice 1

# 1)

def longeur(st):
    return len(st)

# prof
def longeur2(st):
    cmpt = 0
    for lettre in st:
        cmpt = cmpt + 1
    return cmpt


# 2)
# a)

def compte_les_e(st):
    cmpt = 0
    n = len(st)
    for i in range(n):
        if st[i] == "e" :
            cmpt = cmpt + 1
    return cmpt

# prof
def compte_les_e2(st):
    cmpt = 0
    for lettre in st:
        if lettre == "e":
            cmpt = cmpt + 1
    return cmpt


# b)

def occurence(char, st):
    cmpt = 0
    n = len(st)
    for lettre in st:
        if lettre == char:
            cmpt = cmpt + 1
    return cmpt


# c)

# "è" et "ê" != à "e"


## Exercice 2


# 1)

def appartenance_v1(char, st):
    a = False
    n = len(st)
    for i in range(n):
        if st[i] == char:
            a = True
    return a


# 2)

def trouve(char, st):
    a = False
    n = len(st)
    for i in range(n):
        if st[i] == char:
            qds = i
        else:
            ddd = -1
    print(qds)
# a terminer