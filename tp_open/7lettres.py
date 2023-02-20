# Créé par nisars, le 07/04/2022 en Python 3.7

from random import *

fi = open("dico.txt" , "r")

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


print(len(fi.readlines()))
a = randrange(len(fi.readlines()))
print(a)
