# UTF-8 // CRLF // Python3.10.4 64 bit (windows store)
# NISAR Sofiane - HANIFIA Ilyas // P4

from random import randrange

# Pendu avec debug pour voir l'avancement
def pendu_debug():
    nombre_de_mots = 22194
    with open("7lettre.txt", "r", encoding="utf-8") as fi:               # Dictionnaire de base de 7 lettres, en utf-8
            pif = randrange(0, nombre_de_mots + 1)                       # On prend un mot au hasard
            print("Ligne n° :", pif)                                     # Montre le numéro de ligne a des fins de débuggage
            for i in range(pif):
                pick = fi.readline()                                     # Parcours le fichier pour obtenir le mot de la ligne en question
                pick = pick[:-1]                                         # Source (stackoverflow) : https://bit.ly/3ybx93F
            print("Mot à trouver :", pick)
            longueur_du_mot = 7
            essai = 0                                                    # Nombre d'erreurs du joueur  
            liste = list(pick)                                           # Décompose le mot lettre par lettre en liste
            print("Liste du mot :",liste)                                # Montre la liste à des fins de débuggage
            liste_essai = []
            for i in range(longueur_du_mot):
                liste_essai = liste_essai + ["_"]                        # Liste de base pour le pendu ("\n" compris) (7 * "_")
            print(liste_essai)                                           # Montre cette liste de base
            fini = False
            while fini is False:                                         # Tant que le jeu n'est pas fini
                print("Vos essais :", liste_essai)
               
                test = input("Trouve une lettre : ")
                vrai_faux = True

                for u in range(len(liste)):
                    if liste[u] == test:                                 # Si l'indice de la liste du mot est égale à la lettre du joueur
                        print("Une lettre trouvée à l'indice", u)
                        liste_essai[u] = liste[u]
                        vrai_faux = False
                if vrai_faux is True:
                    print("Mauvaise lettre")
                    essai = essai + 1
                    print("essais ratés :", essai)
                if essai == 11:                                          # 11 fautes = fin du jeu (11ème faute fatale)
                    print("Perdu !")
                    print("Le mot était", pick)
                    fini = True                                          # 11 erreurs, fin du jeu
                if liste_essai == liste:
                    print(liste)
                    print("Mot trouvé, bien joué !")
                    print("Le mot était", pick)
                    fini = True                                          # Mot trouvé, fin du jeu

# pendu_debug()


# Jeu réel, sans débug
def pendu():
    nombre_de_mots = 22194
    with open("7lettre.txt", "r", encoding="utf-8") as fi:

            pif = randrange(0, nombre_de_mots + 1)
            for i in range(pif):
                pick = fi.readline()
                pick = pick[:-1]
            longueur_du_mot = 7
            essai = 0
            liste = list(pick)
            liste_essai = []
            for i in range(longueur_du_mot):
                liste_essai = liste_essai + ["_"]
            fini = False

            while fini is False:
                print("Vos essais :", liste_essai)
                test = input("Trouve une lettre : ")
                vrai_faux = True
                for u in range(len(liste)):
                    if liste[u] == test:
                        print("Une lettre trouvée à l'indice", u)
                        liste_essai[u] = liste[u]
                        vrai_faux = False
                if vrai_faux is True:
                    print("Mauvaise lettre")
                    essai = essai + 1
                    print("Essais ratés :", essai)
                if essai == 11:
                    print("Perdu !")
                    print("Le mot était", pick)
                    fini = True
                if liste_essai == liste:
                    print(liste)
                    print("Mot trouvé, bien joué !")
                    print("Le mot était", pick)
                    fini = True

pendu()