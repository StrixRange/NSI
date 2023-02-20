# Créé par nisars, le 23/05/2022 en Python 3.7

# fi.readline().split(';')

# cb d'eleves en p4
# fonction prof qui liste de dico avec chaque ligne
def dos():
    lst = []
    with open("listing.csv", "r", encoding="utf-8") as fi:
        entete = fi.readline()[:-1].split(';')
        # print(entete)
        for i in range(3001):
            d = {}
            ligne = fi.readline()[:-1].split(';')
            for ent, elt in zip(entete, ligne):
                d[ent] = elt
            lst.append(d)
    # print(lst)
    return lst


# fonction qui renvoie le nombre d'eleves en p4
def tres():
    lst = dos()
    caca = 0
    for i in range(3000):
        a = lst[i]['Classe']
        if a == "P4":
            caca += 1
    return caca

# print(tres())


# fonction qui renvoie fichier csv avec les gens et leur infos qui ont la moyenne en maths et NSi
def quatro():
    lst = dos()
    for a in range(3000):
        b = int(lst[a]["Maths"])
        if b >= 10:
            with open("listingmaths.csv", "w", encoding="utf-8") as fi:
                fi.write(str(lst[a]) + "\n")
        c = int(lst[a]["Phyique-Chime"])
        if c >= 10:
            with open("listingpc.csv", "w", encoding="utf-8") as fi:
                fi.write(str(lst[a]))


quatro()




