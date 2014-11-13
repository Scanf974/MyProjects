# -*- coding: utf-8 -*-

from math import *
from scipy import *

class   First_cls(object):
    """Me premier class"""

    def __init__(self, arg1, arg2):
        self.argv1 = arg1
        self.argv2 = arg2

    def fnc(self):
        print self.argv1
        print self.argv2


class   Objet_de_la_vie:
    """Unobjet avec les propriete Newton"""

    def __init__(self, poids, py, px):
        self.poids = poids
        self.py = py
        self.px = px
        t[self.py, self.px] = 1

class   Gland(Objet_de_la_vie):
    """LE gland"""

    def __init__(self, poids, py, px):
        Objet_de_la_vie.__init__(self, poids, py, px)

    def ligne(self, direction):
        if (direction == 6):
            t[self.py, self.px + 1] = 1


def     tab(y0, x0):
    for y in range (y0):
        for x in range (x0):
            print t[y, x],
        print

t = zeros([200, 40], int)
tab(10, 20)
print

g1 = Gland(1, 5, 1)
tab(10, 20)
g1.ligne(6)
tab(10, 20)
