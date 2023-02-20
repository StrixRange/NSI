# Exercice 4

a = int(input("Entrez un entier a : "))

if a % 1 == 0:
    if a % a == 0:
        print("Nombre premier")
else:
    print("Nombre non premier")






# Correction

a = int(input("Entrez un entier a : "))

nombre_premier = True

for i in range(2,n):
    if a % i  == 0:                     # i divise a
        nombre_premier = False

print(nombre_premier)