# 01

# Exercice 1

def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True

verifie([0, 5, 8, 8, 9])
verifie([8, 12, 4])


# Exercice 2

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin]=1
    return resultat

depouille(urne)

def vainqueur(election):
    vainqueur = '' #cette variable ne sert à rien
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat #cette ligne ne sert à rien !
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale