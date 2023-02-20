# Exercice 1

n = int(input("Entrez un entier positif : "))
acc = 1
for i in range(n):
    acc = acc * 2
print(acc)




# Exercice 1, fonction

def ex1(n):
    acc = 1
    for i in range(n):
        acc = acc * 2
    return acc