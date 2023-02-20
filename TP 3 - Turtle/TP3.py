from turtle import *

speed(11)

def exemple():
    forward(150)
    left(120)
    color('red')
    forward(150)
    color('blue')
    goto(0, 0)


# Exercice 1

def carre_ex1():
    """trace un carre de longueur l pixels"""
    for i in range(4):
        forward(1)
        left(90)


# fonction par défaut du carré
def carre(longeur):
    for i in range(4):
        forward(longeur)
        left(90)


# carre()



# Exercice 2

def carre1(longeur):
    x = longeur
    for i in range(10):
        carre(x)
        x = x + 10


# carre1(10)


def carre2(longeur):
    x = longeur
    for i in range(10):
        if i % 2 == 0:
            fillcolor('black')
        else:
            fillcolor('white')
        begin_fill()
        carre(x)
        end_fill()
        x = x - 20


carre2(200)

def carre2prof(longeur):
    x = longeur
    couleur = ['green', 'yellow', 'red']
    for i in range(10):
        fillcolor(couleur[i%3])
        begin_fill()
        carre(x)
        end_fill()
        x = x - 20



def figure3()



done()