#-*-coding: utf-8-*-

from math import sqrt, gcd


class Point2D:
    """ deux attributs
        quatre méthodes..."""

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def affiche(self):
        return f"({self.x} ; {self.y})"

    def distance_a_0(self):
        return sqrt(self.x**2 + self.y**2)

    def distance(self, p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

    def est_confondu(self, C):
        return self.x == p2.x and self.y == p2.y


class Carre:

    def __init__(self, c):
        self.c = c

    def perimetre(self):
        return 4 * self.c

    def aire(self):
        return self.c**2


class Triangle:

    def __init__(self,a,b,c):
        if  a <= b + c and b <= a + c and c <= a + b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('les trois nombres ne forment pas un triangle')

    def aire(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p-self.a)*(p-self.b)*(p-self.c))

    def est_rectangle(self):
        return abs(self.a**2 - self.b**2 - self.c**2) < 10**-15 or \
        (self.b**2 - self.a**2 - self.c**2) < 10**-15 or \
        (self.c**2 - self.b**2 - self.a**2) < 10**-15


class Date:

    nom_mois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', \
     'juin', 'juillet', 'aout', 'septembre', 'octobre', \
     'novembre', 'decembre']

    def __init__(self,j,m,a):
        if 1 <= j <= 31 and 1 <= m <= 12:
            self.j = j
            self.m = m
            self.a = a
        else:
            raise ValueError('date invalide')

    def __str__(self):
        return f'{self.j} {self.nom_mois[self.m-1]} {self.a}'

    def __lt__(self,d2):
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

    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den < 1:
            raise ValueError
        self.num = num
        self.den = den

    def __repr__(self):
        if self.den == 1:
            return f'{self.num}'
        return f'({self.num} / {self.den})'

    def simplifier(self):
        diviseur = gcd(self.num, self.den)
        return Fraction(self.num // diviseur, self.den // diviseur)

    def __eq__(self, f2):
        return  self.num*f2.den == self.den*f2.num

    def __lt__(self, f2):
        return self.num*f2.den < f2.num*self.den

    def __add__(self, f2):
        return Fraction(self.num*f2.den + f2.num*self.den, self.den*f2.den).simplifier()

    def __sub__(self, f2):
        return Fraction(self.num*f2.den - f2.num*self.den, self.den*f2.den).simplifier()

    def __mul__(self, f2):
        if isinstance(f2,int):
            f2 = Fraction(f2, 1)
        return Fraction(self.num*f2.num, self.den*f2.den).simplifier()