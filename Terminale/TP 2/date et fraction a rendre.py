# Exercice 5
print("ccaaca")
class Date:

    """ __str__ renvoie une chaîne de caractères de la forme « 8 mai 1945 »
        __lt__ détermine si une date d1 est antérieure à une date d2 """

    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self,j,m,a):
        if not isinstance(j, int) or j < 1 or j > 31:
            raise ValueError("Les jours doivent être un nombre entier et être compris entre 1 et 31")
        self.j = j
        if not isinstance(m,int) or j < 1 or j > 12:
            raise TypeError('Les mois doivent être un nombre entier et être compris entre 1 et 12')
        self.m = m
        #if m > 12 or m < 1:
            #raise ValueError('pas entre 1 et 12')
        if not isinstance(a, int):
            raise TypeError("Les années doivent être un nombre entier")
        self.a = a

    def __str__(self):
        return str(self.j) + " " + self.month[self.m -1] + " " + str(self.a)

    def __lt__(self, d2):       # d1 < d2 au lieu de a.__lt__(d2)
        if self.a < d2.a:
            return True
        elif self.a > d2.a:
            return False
        elif self.m < d2.m:
            return True
        elif self.m > d2.m:
            return False
        elif self.j < d2.j:
            return True
        else:
            return False




class Fraction:

    """ oiu """

    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numérateur et dénominateur entier uniquement")
        if den <= 0:
            raise ValueError("Dénominateur strictement entier positif uniquement")
        self. num = num
        self.den = den

    def __repr__(self):
        return f'({self.num} / {self.den})'

    def simplifier(self):
        i = 1
        while i <= self.num:
            a = self.num / i
            print(a)

            i = i + 1







