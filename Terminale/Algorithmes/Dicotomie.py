# Dicotomie

def recherche(t, v, g ,d):
    # recherche(t, v, g=0, d=len(t) - 1)
    """Renvoie un indice de la valeur v dans le tableau de nombre t[g--d] (?)
    None sinon
    t supoosé trié dans l'ordre croissant"""

    if g <= d:
        m = (g + d) // 2
        if t[m] > v:
            return recherche(t, v, g, m - 1)
        elif t[m] < v:
            return recherche(t, v, m + 1, d)
        else:
            return m
    else:
        return None

def recherche_dico_recur(t, v):
    return recherche(t, v, 0, len(t)-1)

# -------------------------------------------------------------------------------

def recherche_dico_iteratif(t, v):
    g = 0
    d = len(t) - 1
    while g <= d:
        m = (g + d) // 2
        if t[m] > v:
            d = m - 1
        elif t[m] < v:
            g = m + 1
        else:
            return m
    return None