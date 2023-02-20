# Tri insertion

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        cle = tab[i]
        j = i - 1
        while j >= 0 and cle < tab[j]:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = cle