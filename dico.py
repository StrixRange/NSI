# Créé par nisars, le 16/05/2022 en Python 3.7

# Fonction histogramme prenant en parametre une chaine de caractere st en renvoyant un dico composé de paire lettres occurence

def histogramme(st):
    dico = {}
    for lettre in st:
        if lettre in dico.keys():
            dico[lettre] = dico[lettre] + 1
        else:
            dico[lettre] = 1
    return dico


# Fonction compte_scrabble prenant en parametre une chaine de caractere mot et renvoyant le nombre de point de ce mot au scrabble

def compte_scrabble(mot):
    acc = 0
    dico = {"d":2, "g":2, "m":2, "b":3, "c":3, "p":3, "f":4, "h":4, "v":4, "j":8, "q":8, "k":10, "w":10, "x":10, "y":10, "z":10}
    for i in mot:
        if i in dico:
            acc = acc + dico[i]
        else:
            acc = acc + 1
    print(acc)

compte_scrabble("algerie")


# Fonction Fonction hexa2bin prenant ...