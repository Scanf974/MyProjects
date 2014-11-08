# -*- coding: utf-8 -*-
# Elements graphiques et multimédias
# Codage : Bertrand HOAREAU 

from scipy import *
from Tkinter import *
import time
import winsound
import Tkinter
import threading

class MyTimer:
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


def gestion_missile1():
	bidon = 0

def initialiser():
	bidon = 0
	
def tester():
	bidon = 0

def deplace_gauche():
	bidon = 0

def deplace_droite():
	bidon = 0

def tirer():
	bidon = 0
	
	
def affiche(evt):
	if evt.char=="4": 
		deplace_gauche()
		
	if evt.char=="6":
		deplace_droite()
	
	if evt.char=="q":
		tirer()

# Variables du vaisseau
xv = 100
yv = 400

# Variables alien1

xa = 200
ya = 50

# Gestion missile 1  (envoyé par vaisseau)

flag1 = 0
origine_xm=0
origine_ym=470
xm1=0
ym1=0


fen = Tk()
image_vaisseau1 = PhotoImage(file='vaisseau1.gif')
image_alien1 = PhotoImage(file='alien1.gif')
image_missile1 = PhotoImage(file='missile1.gif')


# Les Timers
timer_missile1 = MyTimer(0.01,gestion_missile1)

# Créer une fenêtre graphique fond noir
can = Canvas(fen, width =500, height =500, bg ='Black')
can.pack(side =TOP, padx =50, pady =50)

# afficher les éléments graphiques (vaisseau, alien, missile)
vaisseau1 = can.create_image(xv, yv, image=image_vaisseau1, anchor=NW)
missile1 = can.create_image(origine_xm,origine_ym, image=image_missile1, anchor=NW)
alien1 = can.create_image(xa,ya, image=image_alien1, anchor=NW)

# Créer des boutons 
b2 = Button(fen, text =' Initialiser ', command =initialiser)
b2.pack(side =LEFT, padx =3, pady =3)

b3 = Button(fen, text =' TESTER ', command =tester)
b3.pack(side =LEFT, padx =8, pady =3)

# Créer une zone pour du texte :
texte=Tkinter.Text(fen, width=70, height=2)
texte.insert(Tkinter.END,'RUN INVADER. Codage : B. Hoareau.  Graphisme : Chloé H ')
texte.pack(side=Tkinter.LEFT)

# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# Pour charger un son
winsound.PlaySound("intro.wav", winsound.SND_ASYNC)


fen.mainloop()
# fen.destroy()

