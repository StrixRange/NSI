# Créé par nisars, le 29/09/2022 en Python 3.7

# tab3 =  tab1 [:]

w = 0

class Tableau:

    def __init__(self, imin, imax, v):
        self.premier = imin
        self.contenu = [v] * (imax - imin + 1)

    def __len__(self):
        return len(self.contenu)

    def __getitem__(self, i):
        return self.contenu[i]