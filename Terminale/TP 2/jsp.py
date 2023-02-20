# Créé par nisars, le 15/09/2022 en Python 3.7

from math import sqrt

class Point3D:

    """ je sais pas"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_a_0(self):
        a = sqrt(x**2 + y**2 + z**2)
        return a

    def distance_2P(self, point):
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)

    def affichage(self):
        return f'x : {self.x} -- y : {self.y} -- z : {self.z}'

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y and self.z == point.z


    # distance2p shell
    # >>> A = Point3D(1,0,0)
    #>>> O = Point3D(0,0,0)
    #>>> A.distance_2p(O)
    #1.0
    #>>> B = Point3D(1,0,0)
    #>>> A.distance_2p(B)
    #0.0