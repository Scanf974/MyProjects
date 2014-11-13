# -*- coding: utf-8 -*-


from Tkinter import *
from math import *
from scipy import *
import ImageTk
import threading

class   MyTimer:
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)

    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()


class   Objet_de_la_vie:
    """Unobjet avec les propriete Newton"""

    def __init__(self, poids, coeff, py0, px0):
        self.poids = poids
        self.py0 = py0
        self.px0 = px0
        self.py = py0
        self.px = px0
        self.coeff = coeff
        self.timer = MyTimer(0.001, self.deplace)

    def shoot(self, vitesse, angle):
        self.angle = angle
        self.vitesse = vitesse
        self.vx = cos(self.angle*0.0174) * vitesse
        self.vy = sin(self.angle*0.0174) * vitesse
        self.tps = 0
        self.timer.start()

    def deplace(self):

        if (self.vitesse > 2):
            if (self.py > 340):
                self.px0 = self.px
                self.py0 = 340
                self.vitesse *= self.coeff
                self.timer.stop()
                self.shoot(self.vitesse, self.angle)

            if (self.px > -20 and self.px < 1000):
                self.px = self.vx*self.tps + self.px0
                self.py = ((self.poids*9.81)/2)*self.tps*self.tps - self.vy*self.tps + self.py0
                can.coords(self.image, self.px, self.py)
                self.tps += 0.018
        else:
            self.timer.stop()



class   Gland(Objet_de_la_vie):
    """LE gland"""

    def __init__(self, poids, coeff, py, px):
        Objet_de_la_vie.__init__(self, poids, coeff, py, px)
        self.image = can.create_image(self.px, self.py, image = gland_image, anchor = NW)
class   Squirrel(Objet_de_la_vie):
    """LE squirrel"""

    def __init__(self, poids, coeff, py, px):
        Objet_de_la_vie.__init__(self, poids, coeff, py, px)
        self.image = can.create_image(self.px, self.py, image = squirrel_image, anchor = NW)


#----------------PROGRAMME PRINCIPALE---------------

#creation canvas
fen = Tk()
fen.title("BallSquirrel")
frame = Frame(fen)
frame.pack()
can = Canvas(fen, width = 1200, height = 500, bg = 'white')
can.pack(side = TOP, padx = 0, pady = 0)

#url des images
gland_image = ImageTk.PhotoImage(file = 'images/gland.png')
squirrel_image = ImageTk.PhotoImage(file = 'images/ab.png')
fond_image = ImageTk.PhotoImage(file = 'images/decors.png')
sol_image = ImageTk.PhotoImage(file = 'images/bg2.png')

#implantation image de base
fond = can.create_image(0, 0, image = fond_image, anchor = NW)
sol = can.create_image(0, 351, image = sol_image, anchor = NW)

g1 = Gland(1, 0.1, 100, 400)
sq = Squirrel(1, 0.3, 300, 50)

sq.shoot(80.0, 74)

#kill de la fenetre
fen.mainloop()
