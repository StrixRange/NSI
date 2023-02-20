# Exercice 5

a = int(input("Entrez un nombre a : "))
b = int(input("Entrez un nombre b : "))

if a == 0 or b == 0:
    print("le produit est nul")
elif (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Le produit de ces deux nombres sera strictement positif")
else:
    print("Le produit de ces deux nombres sera strictement négatif")

