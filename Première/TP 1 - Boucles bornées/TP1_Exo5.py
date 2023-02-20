# Exercice 5

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