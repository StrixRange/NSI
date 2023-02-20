# -*- coding: utf-8 -*-


def moyenne(tab):
    somme_note = 0
    somme_coeff = 0
    for note, coeff in tab:
        somme_note += note*coeff
        somme_coeff += coeff
    return None if somme_coeff == 0 else somme_note/somme_coeff 

    