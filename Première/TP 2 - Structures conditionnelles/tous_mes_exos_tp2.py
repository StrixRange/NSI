# Exercice 1

a = int(input("Entrez un entier a : "))
b = int(input("Entrez un entier b : "))

if a < b:
    print(a)
else:
    print(b)





# Exercice 2

a = int(input("Entrez un entier a : "))

if a % 2 == 0:
    print("Pair")
else:
    print("Impair")

# Avec booléens

a = int(input("Entrez un entier a : "))

pair = nb % 2

if pair == 0:
    print("Nombre pair")
else:
    print("Nombre impair")





# Exercice 3
# Correction

a = int(input("Entrez un entier a : "))

for i in range(1,a+1):
    if a % i == 0:
        print(i)





# Exercice 4
# Correction

a = int(input("Entrez un entier a : "))

nombre_premier = True

for i in range(2,n):
    if a % i  == 0:                     # i divise a
        nombre_premier = False

print(nombre_premier)





# Exercice 5

a = int(input("Entrez un nombre a : "))
b = int(input("Entrez un nombre b : "))

if a == 0 or b == 0:
    print("le produit est nul")
elif (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Le produit de ces deux nombres sera strictement positif")
else:
    print("Le produit de ces deux nombres sera strictement négatif")





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





# FIN