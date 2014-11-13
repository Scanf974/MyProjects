# -*- coding: utf-8 -*-

from Tkinter import *
from math import *
from scipy import *
import ImageTk

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

class   Gland(Objet_de_la_vie):
    """LE gland"""

    def __init__(self, poids, py, px):
        Objet_de_la_vie.__init__(self, poids, py, px)
        self.image = can.create_image(self.px, self.py, image = gland_image, anchor = NW)

class   Squirrel(Objet_de_la_vie):
    """LE squirrel"""

    def __init__(self, poids, py, px):
        Objet_de_la_vie.__init__(self, poids, py, px)
        self.image = can.create_image(self.px, self.py, image = squirrel_image, anchor = NW)


fen = Tk()
fen.title("BallSquirrel")
frame = Frame(fen)
frame.pack()

can = Canvas(fen, width = 1200, height = 500, bg = 'white')
can.pack(side = TOP, padx = 0, pady = 0)

gland_image = ImageTk.PhotoImage(file = 'images/gland.png')
squirrel_image = ImageTk.PhotoImage(file = 'images/ab.png')
fond_image = ImageTk.PhotoImage(file = 'images/decors.png')
sol_image = ImageTk.PhotoImage(file = 'images/bg2.png')

fond = can.create_image(0, 0, image = fond_image, anchor = NW)
sol = can.create_image(0, 351, image = sol_image, anchor = NW)

g1 = Gland(1, 100, 400)
sq = Squirrel(1, 300, 50)

fen.mainloop()
