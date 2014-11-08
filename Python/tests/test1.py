# -*- coding: utf-8 -*-

from math import *

class   First_cls(object):
    """Me premier class"""

    def __init__(self, arg1, arg2):
        self.argv1 = arg1
        self.argv2 = arg2

    def fnc(self):
        print self.argv1
        print self.argv2


class   Gland(object):
    """LE gland"""

    def     __init__(self, vitesse, angle, py, px):
        self.vitesse = vitesse
        self.angle = angle
        self.py = py
        self.px = px

    def     init_vitesse(vitesse, angle, py, px):
        angle_rad = 0.0174*angle
        vy = sin(angle_rad)
        vx = cos(angle_rad)


g1 = Gland(80, 25, 10, 10)
yo = First_cls("Hey mecdfgsdfg", "Gros PD")
yo.fnc()

