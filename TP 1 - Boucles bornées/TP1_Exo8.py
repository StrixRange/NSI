# Exercice 8

# Début de la suite de Fibonacci : 1 1 2 3 5 8 13 21 34 45

n = int(input("Entrez un entier n > 2 : "))
a = 0
b = 1

for i in range(n-1):
    c = a + b
    a = b
    b = c

print(c)