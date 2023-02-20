from random import *

# 336532 lignes

def lettres7():
    with open("dico.txt", "r") as fi:
        with open("7lettre.txt", 'w') as fi2:
            flag = True
            while flag is True:
                mot = fi.readline()
                if len(mot) == 0:
                    flag = False
                elif len(mot) == 8:
                    fi2.write(mot)

def pif():
    pif = randrange(0, 336532)
    return pif


def pendu2():
    with open("dico.txt", "r") as fi:
        with open("7lettre.txt", 'w') as fi2:
            flag = True
            while flag is True:
                mot = fi.readline()
                if len(mot) == 0:
                    flag = False
                elif len(mot) == 8:
                    fi2.write(mot)
            pif = randrange(0, 336532)
            essai = 0
            essai_max = 11
            mot2 = fi.readlines()
            print(mot2)
        fi.seek(2)
        mot3 = fi.readline()
        print(mot3)


# FONCTIONNE
def pendu3():
    with open("7lettre.txt", "r", encoding="utf-8") as fi:
            pif = randrange(0, 22195)
            print(pif)
            for i in range(pif):
                pick = fi.readline()
            print(pick)
            essai = 0
            essai_max = 11
            liste = list(pick)
            print(liste)
            liste_essai = ["_", "_", "_", "_", "_", "_", "_"]
            fini = True
            while fini is True:
                print(liste_essai)
                test = input("Trouve une lettre : ")
                for u in range(len(liste)):
                    if liste[u] == test:
                        print("1 Lettre trouvée")
                        liste_essai[u] = liste[u]
                        #fini = False


#                    else:
#                        essai = essai + 1
#                        if essai == essai_max:
#                            print("Perdu")
#                            fini = False


pendu3()
