#-*-coding: utf-8-*-


tree1 = [7,[3,[2,[1,[],[]],[5,[],[]]],[]],[4,[6,[],[]],[8,[],[]]]]


def taille(arbre):
    if arbre == []:
        return 0
    return 1 + taille(arbre[1]) + taille(arbre[2])


def hauteur(arbre):
    if arbre == []:
        return 0
    return 1 + max(hauteur(arbre[1]), hauteur(arbre[2]))


def parcours_prefixe(arbre):
    if arbre == []:
        return None
    print(arbre[0], end=" - ")
    parcours_prefixe(arbre[1])
    parcours_prefixe(arbre[2])


def parcours_infixe(arbre):
    if arbre == []:
        return None
    parcours_infixe(arbre[1])
    print(arbre[0], end=" - ")
    parcours_infixe(arbre[2])


def parcours_postfixe(arbre):
    if arbre == []:
        return None
    parcours_postfixe(arbre[1])
    parcours_postfixe(arbre[2])
    print(arbre[0], end=" - ")


print(taille(tree1))
print(hauteur(tree1))
print(parcours_prefixe(tree1))
print()
print(parcours_infixe(tree1))
print()
print(parcours_postfixe(tree1))
