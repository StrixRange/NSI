# Exercice 6

# 1)
# Écrire un programme qui demande à l’utilisateur un nombre de chiffres n puis n chiffres, et qui calcule et affiche le nombre formé avec les n chiffres dans l’ordre.

# Correction

n = int(input("Nombre de chiffre N ? "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre "))
    nombre = nombre * 10 + chiffre

print(nombre)



# Fonction (???)

def ex61(n, chiffre):
    nombre = 0
    for i in range(n):
        chiffre = int(input("Saisir un chiffre "))
        nombre = nombre * 10 + chiffre
    return nombre





# 2)
# Écrire une variante du même programme dans lequel les chiffres sont donnés dans l’ordre inverse.

n = int(input("Nombre de chiffre N ? "))
nombre = 0

for i in range(n):
    chiffre = int(input("Saisir un chiffre "))
    nombre = nombre * 10 + chiffre

print(nombre)



# Fonction (???)

def ex62(n, chiffre):
    nombre = 0
    for i in range(n):
        chiffre = int(input("Saisir un chiffre "))
        nombre = nombre * 10 + chiffre
    return nombre