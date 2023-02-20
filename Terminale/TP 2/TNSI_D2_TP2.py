# Créé par nisars, le 19/09/2022 en Python 3.7
# TNSI_D2_TP2


# Exercice 1
from math import sqrt

class Point2D:

    """ bonne question"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def affiche(self):
        # return self.x, ";", self.y
        return f'({self.x} ; {self.y})'

    def distance_a_0(self):
        return sqrt(self.x**2 + self.y**2)

    def distance(self, B):
        return sqrt((B.x - self.x)**2 + (B.y - self.y)**2)

    def est_confondu(self):
        return self.x == B.x and self.y == B.y


# Exercice 2

class Carre:

    """ jsp """

    def __init__(self, l):
        self.l = l

    def perimetre(self):
        return 4*self.l

    def aire(self):
        return self.l * self.l


# Exercice 3

class Triangle:

    """ où c est l'hypothénuse """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def aire(self):
        p = self.a + self.b + self.c
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def est_rectangle(self):
        return self.c**2 == self.a**2 + self.b**2


# Exercice 4

class Temps:

    """ tkt"""

    #from time import *


    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def affiche(self):
        return f'{self.hh} h {self.mm} min {self.ss} ss'

    def __add__(self, B):
        #w = self.hh + B.hh
        #x = self.mm + B.mm
        #z = self.ss + B.mm

        if B.ss > 60:
            a = B.ss - 60
            B.mm + "jsp"


# Exercice 5

class Date:

    """ dsqkfoish """

    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self,j,m,a):
        self.j = j
        if not isinstance(m,int):
            raise TypeError('pas entier')
        if m > 12 or m <1:
            raise ValueError('pas entre 1 et 12')
        self.m = m
        self.a = a

    def __str__(self):
        return str(self.j) + " " + self.month[self.m -1] + " " + str(self.a)

    def __lt__(self, d2):       # d1 < d2 au lieu de a.__lt__(d2)
        if self.a < d2.a:
            return True
        elif self.a > self.d2:
            return False
        elif self.m < d2.m:
            return True
        elif self.m > d2.m:
            return False
        elif self.d < d2.d:
            return True
        else:
            return False




class Fraction:

    """ sqdqds """

    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f'{self.num} / {self.den}'

    def __add__(self, f2):
        return Fraction(self.num * f2.den + f2.num * self.den, self.den * f2.den)

    def simplifier(self):
        diviseur = gcd(self.num, self.den)
        return Fraction(self.num // diviseur, self.den // diviseur)


