# -*-coding: utf-8-*-


class Tableau:
    """Documentation for Tableau"""

    def __init__(self, imin, imax, v):
        self.premier = imin
        self.contenu = [v] * (imax - imin + 1)

    def __len__(self):
        return len(self.contenu)

    def __getitem__(self, i):
        if i < self.premier or i > self.premier + len(self.contenu) - 1:
            raise IndexError(i)
        return self.contenu[i - self.premier]

    def __setitem__(self, i, v):
        if i < self.premier or i > self.premier + len(self.contenu) - 1:
            raise IndexError(i)
        self.contenu[i - self.premier] = v

    def __str__(self):
        return "| " + " | ".join(map(str, self.contenu)) + " |"


class TabBiDir:
    """Documentation for TabBiDir"""

    def __init__(self, g, d):
        self.g = g[:] # on recopie le tableau g dans self.g
        self.d = d[:]

    def imin(self):
        return -1 * len(self.g)

    def imax(self):
        return len(self.d) - 1

    def append(self, v):
        self.d.append(v)

    def prepend(self, v):
        self.g.append(v)

    def __getitem__(self, i):
        if i < 0:
            return self.g[-(i+1)]
        return self.d[i]

    def __setitem__(self, i, v):
        if i < 0:
            self.g[-(i+1)] = v
        else:
            self.d[i] = v

    def __str__(self):
        fmt = " | ".join(map(str, self.g[::-1])) + " | " + \
            " | ".join(map(str, self.d))
        return fmt
