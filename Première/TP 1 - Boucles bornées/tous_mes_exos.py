# Exercices 1 à 8 - TP 1

## Exercice 1

n = int(input("Entrez un entier positif : "))
acc = 1
for i in range(n):
    acc = acc * 2
print(acc)


## Exercice 2


#acc = 1
#for i in range(101):
#    acc = acc * 100
#print(acc)



acc = 1
for i in range(1,101):
    acc = acc * i
print(acc)


## Exercice 3

n = int(input("Entrez un entier positif : "))
acc = 0
for i in range(1,n+1):
    acc = acc + i

print(acc)
print(n*(n+1)//2)


## Exercice 4

s = int(input("Entrez la somme S déposée sur votre livret : "))
t = int(input("Entrez les taux d'intêrets annuel T déposée sur votre livret, en % : "))
n = int(input("Entrez le nombre d'année N : "))

for i in range(n):
    interet = s * (t / 100)
    s = s + interet

print(s)
# print(interet) ???


## Exercice 5

# Sans coefficient = 1

n2 = 0
n = int(input("Nombre de notes N ? "))

for i in range(n):
    n1 = float(input("Note de l'élève ? "))
    n2 = n1 + n2

print(n2 / n)



# Avec coefficient = c

n2 = 0
somme_coeff = 0
n = int(input("Nombre de notes N ? "))
c = float(input("Coefficient ? "))

for i in range(n):
    n1 = float(input("Note de l'élève ? "))
    coeff = float(input("Coefficient ? "))
    n2 = n2 + n1 * coeff
    somme_coeff = somme_coeff + coeff

print(n2 / somme_coef)


## Exercice 6

# 1)
# Écrire un programme qui demande à l’utilisateur un nombre de chiffres n puis n chiffres, et qui calcule et affiche le nombre formé avec les n chiffres dans l’ordre.

n = int(input("Nombre de chiffre N ? "))
n2 = 0

for i in range(n)
    n1 = int(input("N chiffre ? "))
    n2 = n1 * 10**


# Correction

n = int(input("Nombre de chiffre N ? "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre "))
    nombre = nombre * 10 + chiffre

print(nombre)


# 2)
# Écrire une variante du même programme dans lequel les chiffres sont donnés dans l’ordre inverse.

n = int(input("Nombre de chiffre N ? "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre "))
    nombre = nombre * 10 + chiffre

print(nombre)


## Exercice 7

nombre_entier = int(input("Entrez un nombre entier : "))
k = int(input("Entrez un nombre de chiffre k : "))

for i in range(k):
    resultat = nombre_entier % 10
    print(resultat)
    diviseur = nombre_entier // 10
    nombre_entier = diviseur


## Exercice 8

# Début de la suite de Fibonacci : 1 1 2 3 5 8 13 21 34 45

n = int(input("Entrez un entier n > 2 : "))
a = 0
b = 1

for i in range(n-1):
    c = a + b
    a = b
    b = c

print(c)


##
##Fin