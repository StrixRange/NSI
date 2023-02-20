# Créé par nisars, le 31/03/2022 en Python 3.7

fi = open("multiplication.txt" , "w")

for j in range(1,11):
    fi.write(f"Table de {j} :\n")
    for i in range(1, 11):
        fi.write(f"{i} x {j} = {i*j}\n")
    fi.write("\n")

fi.close()