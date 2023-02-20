# Créé par nisars, le 04/04/2022 en Python 3.7

def triangle_gauche(nb):
    with open("deco.txt", "w") as fi:
        for i in range(nb):
            fi.write("*"*(i+1) + "\n")


def triangle_droite(nb):
    with open("deco.txt", "w") as fi:
        for i in range(nb-1, -1, -1):
            fi.write(" "*i + "*" * (nb-i) + "\n")

triangle_droite(5)

