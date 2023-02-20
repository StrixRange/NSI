# Exercice 3

a = int(input("Entrez un entier a : "))

for i in range(1,a):
    if a % i == 0:
        print(a // i)






# Correction

a = int(input("Entrez un entier a : "))

for i in range(1,a+1):
    if a % i == 0:
        print(i)