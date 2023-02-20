#-*-coding: utf-8-*-

from math import sqrt


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










