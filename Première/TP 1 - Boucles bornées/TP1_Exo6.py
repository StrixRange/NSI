# Exercice 6

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