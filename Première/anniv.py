from random import randrange

def classe():
    return [randrange(1, 366) for i in range(23)]

def doublon(classe):
    return len(classe) != len(set(classe))

def simul(nb_total):
    cpt = 0
    for i in range(nb_total):
        cl = classe()
        if doublon(cl):
            cpt = cpt + 1
    return cpt / nb_total

nb_total = 100000
print(simul(nb_total))

def doublon2(lst):
    a = False
    n = len(lst)
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] == lst[j]:
                a = True
    return a



def doublon3(lst):
    lst2 = []
    for item not in lst2:
        lst2.append(item)
    else:
        return True
    return False