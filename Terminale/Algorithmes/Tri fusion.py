# Tri fusion

def fusion(l1, l2):
    """ Renvoie un tableau trié contenant les valeurs de l1 et l2
    rangés dans l'ordre croissant """

    l3 = []
    n1, n2 = len(l1), len(l2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    while i < n1:
        l3.append(l1[i])
        i += 1
    while j < n2:
        l3.append(l2[j])
        j += 1
    return l3


def fusion_V2(l1, l2):
    """ Renvoie un tableau trié contenant les valeurs de l1 et l2,
    supposés trié dans l'ordre croissant à l'aide de sentinelles """

    n = len(l1) + len(l2)
    l3 = [0] * n
    i, j = 0, 0
    l1.append(float("inf"))
    l2.append(float("inf"))
    for k in range(n):
        if l1[i] <= l2[j]:
            l3[k] = l1[i]
            i += 1
        else:
            l3[k] = l2[j]
            j += 1
    return l3


def fusion_recur(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + fusion_recur(l1[1:], l2)
    else:
        return [l2[0]] + fusion_recur(l1, l2[1:])