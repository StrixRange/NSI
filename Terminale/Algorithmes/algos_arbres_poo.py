#-*-coding: utf-8-*-


class Node:

    def __init__(self, v, g=None, d=None):
        self.val = v
        self.fg = g
        self.fd = d


tree1 = Node(7, Node(3, Node(2, Node(1), Node(5))), Node(4, Node(6), Node(8)))


def taille(arbre):
    if arbre is None:
        return 0
    return 1 + taille(arbre.fg) + taille(arbre.fd)


def hauteur(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.fg), hauteur(arbre.fd))


def parcours_prefixe(arbre):
    if arbre is None:
        return None
    print(arbre.val, end=" - ")
    parcours_prefixe(arbre.fg)
    parcours_prefixe(arbre.fd)


def parcours_infixe(arbre):
    if arbre is None:
        return None
    parcours_infixe(arbre.fg)
    print(arbre.val, end=" - ")
    parcours_infixe(arbre.fd)


def parcours_postfixe(arbre):
    if arbre is None:
        return None
    parcours_postfixe(arbre.fg)
    parcours_postfixe(arbre.fd)
    print(arbre.val, end=" - ")


print(taille(tree1))
print(hauteur(tree1))
print(parcours_prefixe(tree1))
print()
print(parcours_infixe(tree1))
print()
print(parcours_postfixe(tree1))


