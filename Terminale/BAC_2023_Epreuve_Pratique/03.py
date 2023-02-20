# 03

# Exercice 1

def moyenne(tab):
    acc = 0
    b = 0
    for j in range(len(tab)):
        b = b + tab[j][1]
    if b == 0:
        return None
    for i in range(len(tab)):
        acc = acc + tab[i][0] * tab[i][1]
    return acc / b

def moyenne_V2(tab):
    s_valeur = 0
    s_coef = 0
    for v in tab:
        s_valeur = s_valeur + v[0]*v[1]
        s_coef = s_coef + v[1]
    if s_coef == 0:
        return None
    else :
        return s_valeur/s_coef

def moyenne_ProfVac(tab):
    somme_note = 0
    somme_coeff = 0
    for note, coeff in tab:
        somme_note += note*coeff
        somme_coeff += coeff
    return None if somme_coeff == 0 else somme_note/somme_coeff 


# Exercice 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end= "")
            else:
                print("  ", end= "")
        print()

def zoomListe(liste_depart, k):
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
