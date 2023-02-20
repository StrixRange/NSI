# Exercice 6, validé

annee = int(input("Saisir une année : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):             # != veut dire "non égal à"
    print(annee, "est une année bissextile")
else:
    print(annee, "n'est pas une année bissextile")





# """Meilleure""" version :

annee = int(input("Saisir une année : "))
bissextile = False

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    bissextile = True

print(bissextile)

