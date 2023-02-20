# -*-coding: utf-8-*-

import turtle as tt


def carre(dist):
    for i in range(4):
        tt.forward(dist)
        tt.left(90)


def fenetre(dist):
    tt.fillcolor('yellow')
    tt.begin_fill()
    for i in range(4):
        tt.forward(dist)
        tt.left(90)
    tt.end_fill()


def rectangle(larg, haut):
    tt.fillcolor('grey')
    tt.begin_fill()
    for i in range(2):
        tt.forward(larg)
        tt.left(90)
        tt.forward(haut)
        tt.left(90)
    tt.end_fill()


def polygone(nb_cote, dist):
    for i in range(nb_cote):
        tt.forward(dist)
        tt.left(360/nb_cote)


def demi_cercle(rayon, couleur):
    tt.color(couleur)
    tt.circle(rayon, extent=180)


def figure1():
    cote = 200
    while cote >= 20:
        carre(cote)
        cote = cote - 20


def figure2():
    cote = 200
    cpt = 0
    while cote >= 20:
        if cpt % 2 == 0:
            tt.fillcolor('black')
        else:
            tt.fillcolor('white')
        tt.begin_fill()
        carre(cote)
        tt.end_fill()
        cote = cote - 20
        cpt = cpt + 1


def figure2bis():
    cote = 200
    cpt = 0
    couleurs = ['red', 'yellow', 'green', 'purple']
    n = len(couleurs)
    while cote >= 20:
        tt.fillcolor(couleurs[cpt % n])
        tt.begin_fill()
        carre(cote)
        tt.end_fill()
        cote = cote - 20
        cpt = cpt + 1


def figure3():
    cote = 100
    for i in range(10, 2, -1):
        polygone(i, cote)


def figure4():
    cote = 100
    for i in range(10, 2, -1):
        if i % 2 == 0:
            tt.fillcolor('black')
        else:
            tt.fillcolor('white')
        tt.begin_fill()
        polygone(i, cote)
        tt.end_fill()


def figure4bonus():
    rayon = 160
    cpt = 0
    while rayon >= 20:
        if cpt % 2 == 0:
            tt.fillcolor('black')
        else:
            tt.fillcolor('white')
        tt.begin_fill()
        tt.circle(rayon)
        tt.end_fill()
        rayon = rayon - 20
        cpt = cpt + 1


def figure5(nb_arcs):
    rayon = 120
    coul = [1, 0, 0]
    for i in range(nb_arcs):
        demi_cercle(rayon, coul)
        tt.up()
        tt.home()
        tt.down()
        tt.left(360/nb_arcs * (i+1))
        coul[0] = coul[0] - 1/(nb_arcs-1)
        coul[2] = coul[2] + 1/(nb_arcs-1)


def figure6():
    cote = 20
    rectangle(7*cote, 15*cote)
    for j in range(7):
        tt.up()
        tt.goto(cote, (2*j+1)*cote)
        tt.down()
        for i in range(3):
            fenetre(cote)
            tt.up()
            tt.forward(2*cote)
            tt.down()
    tt.up()
    tt.home()
    tt.down()


tt.speed(11)

# figure1()
# figure2()
# figure2bis()
# figure3()
# figure4()
# figure4bonus()
# figure5(100)
# figure6()

tt.done()
