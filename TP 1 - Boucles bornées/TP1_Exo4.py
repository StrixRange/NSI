# Exercice 4

s = int(input("Entrez la somme S déposée sur votre livret : "))
t = int(input("Entrez les taux d'intêrets annuel T déposée sur votre livret, en % : "))
n = int(input("Entrez le nombre d'année N : "))

for i in range(n):
    interet = s * (t / 100)
    s = s + interet

print(s)
# print(interet) ???