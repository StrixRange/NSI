# 07

# Exercice 1

# Voir tri fusion


# Exercice 2

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ RECURSIF
    Renvoie l’écriture décimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= 2:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]