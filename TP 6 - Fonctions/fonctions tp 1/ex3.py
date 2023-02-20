# Exercice 3

n = int(input("Entrez un entier positif : "))
acc = 0
for i in range(1,n+1):
    acc = acc + i

print(acc)
print(n*(n+1)//2)




# Exercice 3, fonction

def ex2(n):
    acc = 0
    for i in range(1,n+1):
        acc = acc + i
    print(n*(n+1)//2)
    return acc