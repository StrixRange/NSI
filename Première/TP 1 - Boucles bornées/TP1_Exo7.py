# Exercice 7

nombre_entier = int(input("Entrez un nombre entier : "))
k = int(input("Entrez un nombre de chiffre k : "))

for i in range(k):
    resultat = nombre_entier % 10
    print(resultat)
    diviseur = nombre_entier // 10
    nombre_entier = diviseur