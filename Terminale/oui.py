# Créé par nisars, le 06/09/2022 en Python 3.7

def division_euclidienne(a, b):
    """ Renvoie le quotient de a par b, en renvoyant le résultat et le reste de cette division"""
    q = 0
    r = a
    while r >= b:
        q = q + 1
        r = r - b
    return q, r

print(division_euclidienne(10,3))
