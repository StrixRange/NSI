# -*-coding: utf-8-*-








# Exercice 1

n = int(input("Saisir un entier positif : "))
resultat = 1

for _ in range(n):
    resultat = resultat * 2

print(resultat)







# Exercice 2

resultat = 1

for i in range(1, 101):
    resultat = resultat * i

print(resultat)







# Exercice 3

n = int(input("Saisir un entier positif : "))
resultat = 0

for i in range(1, n+1):
    resultat = resultat + i

print(resultat)
print(resultat == n*(n+1)/2)  # comparaison du resultat avec la formule donnée







# Exercice 4

s = float(input("Saisir une capital à placer : "))
t = float(input("Saisir un taux d'intérêt (en %) : "))
n = int(input("Saisir un nombre d'années : "))

for _ in range(n):
    interets = s * (t/100)
    print(interets)
    s = s + interets

print(s)








# Exercice 5

# Calcul de la moyenne non pondérée de n notes

n = int(input("Saisir un nombre de notes : "))
somme_notes = 0

for _ in range(n):
    note = float(input("Saisir une note :"))
    somme_notes = somme_notes + note

print(somme_notes / n)

# Calcul de la moyenne pondérée de n notes

n = int(input("Saisir un nombre de notes : "))
somme_notes = 0
somme_coeff = 0

for _ in range(n):
    note = float(input("Saisir une note (sur 20) : "))
    coeff = float(input("Saisir un coefficient : "))
    somme_notes = somme_notes + note * coeff
    somme_coeff = somme_coeff + coeff

print(somme_notes / somme_coeff)








# Exercice 6

# Question 1 version 1

n = int(input("Saisir un nombre de chiffres : "))
nombre = 0

for _ in range(n):
    chiffre = int(input("Saisir un chiffre : "))
    nombre = nombre * 10 + chiffre

print(nombre)



# Question 1 version 2

n = int(input("Saisir un nombre de chiffres : "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre : "))
    nombre = nombre + chiffre * 10**(n-1-i)

print(nombre)




# Question 2

n = int(input("Saisir un nombre de chiffres : "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre : "))
    nombre = nombre + chiffre * 10**i

print(nombre)








# Exercice 7

n = int(input("Saisir un nombre : "))
k = int(input("Saisir un nombre de chiffres : "))

for _ in range(k):
    print(n % 10)
    n = n // 10








# Exercice 8

n = int(input("Saisir l'indice souhaité (>1) : "))
a = 0
b = 1

for _ in range(n-1):
    c = a + b
    a = b
    b = c

print("Le terme de rang {} de la suite de fibonacci est : {}".format(n, c))
