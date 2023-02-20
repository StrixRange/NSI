# -*- coding: utf-8 -*-


tab = [1, 1, 1, 0] # 1*2**3 + 1*2**2 + 1*2**1 + 0*2**0


def convertir(tab):
    acc = 0
    dim = len(tab)
    for i in range(dim):
        acc = acc + tab[i] * 2**(dim-1-i)
    return acc


assert convertir(tab) == 14
    
    

