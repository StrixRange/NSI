# Créé par nisars, le 07/04/2022 en Python 3.7

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

def pendu():
    lettres7()
    pif()
    essai = 0
    essai_max = 11
    for i in range(pif):
        mot = fi.readline
    print(mot)




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
            for i in range(pif):
                fi.readline(pif)
            print(mot)


