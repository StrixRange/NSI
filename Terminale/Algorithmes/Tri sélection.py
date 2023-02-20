# Tri sélection

def tri_selection(tab):
    n = len(tab)
    for i in range(n - 1):
        ind_min = i
        for j in range(i + 1, n):
            if tab[j] < tab[ind_min]:
                ind_min = j
            tab[i], tab[ind_min] = tab[ind_min], tab[i]