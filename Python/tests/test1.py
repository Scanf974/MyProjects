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
        self.moov = 0
        self.timer = MyTimer(0.001, self.deplace)

    def shoot(self, vitesse, angle):
        self.angle = angle
        self.vitesse = vitesse
        self.vx = cos(self.angle*0.0174) * vitesse
        self.vy = sin(self.angle*0.0174) * vitesse
        self.tps = 0
        self.timer.start()

    def deplace(self):
        self.moov = 1
        if (self.vitesse > 2):
            if (self.py > 340):
                self.timer.stop()
                self.px0 = self.px
                self.py0 = 340
                self.vitesse *= self.coeff
                self.shoot(self.vitesse, self.angle)

            if (self.px < -20):
                self.vx = -self.vx
                self.px = -20
                self.angle = self.angle - 2*(self.angle - 90)
                self.px0 = -20 - self.px0
            elif (self.px > 1000):
                self.vx = -self.vx
                self.px = 1000
                self.angle = self.angle - 2*(self.angle - 90)
                self.px0 = 2*1000 - self.px0

            if (self.px >= -20 and self.px <= 1000):
                self.px = self.vx*self.tps + self.px0
                self.py = ((self.poids*9.81)/2)*self.tps*self.tps - self.vy*self.tps + self.py0
                can.coords(self.image, self.px, self.py)
                self.tps += 0.018
        else:
            self.moov = 0
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


def     pointeur(event):
    x,y = event.x,event.y

    print "click"
    i = 0
    vitesse = 0
    angle = 0
    while (sq[i]):
        if (sq[i].moov == 0):
            oppose = sq[i].py0 + 30 - y
            if (x < sq[i].px0 + 30):
                adjacent = (sq[i].px0 + 30 - x)
                tanj = oppose / adjacent
                angle = 180 - math.degrees(math.atan(tanj))
                h = -adjacent / cos(angle*0.0174)
            elif (x > sq[i].px0 + 30):
                adjacent = x - sq[i].px0 + 30
                tanj = oppose / adjacent
                angle = math.degrees(math.atan(tanj))
                h = adjacent / cos(angle*0.0174)
            vitesse = h * 0.2
            if (vitesse >= 90):
                vitesse = 90
            sq[i].shoot(vitesse, angle)
        i = i + 1
#----------------PROGRAMME PRINCIPALE---------------

#creation canvas
fen = Tk()
fen.title("BallSquirrel")
frame = Frame(fen)
frame.pack()
can = Canvas(fen, width = 1200, height = 500, bg = 'white')
can.bind("<Button-1>", pointeur)
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
sq = [Squirrel(1, 0.3, 340, 50),
        Squirrel(1, 0.3, 340, 550),
        Squirrel(1, 0.3, 340, 150),
        0]

#kill de la fenetre
fen.mainloop()
