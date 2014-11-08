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


def arreter_missile():
	global flag1
	can.coords(missile1, origine_xm, origine_ym)			
	flag1=0
	timer_missile1.stop()

def tester_collision(x,y):
	global xa,ya		# Alien qui va exploser
	
	if flag1==1:
		if x>xa and x<xa+45 and y>ya and y<ya+75 :
			can.delete(alien1)
			arreter_missile()
			winsound.PlaySound("boum1.wav", winsound.SND_ASYNC)
			xa=-100		
			ya=-100



def gestion_missile1():
	global xm1,ym1,flag1,stage_fin_niveau
	if flag1==1:
		if ym1>10:
			ym1 = ym1 - 10
			can.coords(missile1, xm1, ym1)
			tester_collision(xm1,ym1)

			
		else:
			can.coords(missile1, origine_xm, origine_ym)			
			flag1=0
			timer_missile1.stop()

def initialiser():
	can.create_rectangle(10, 10, 50, 50, outline="white", fill='yellow')
	can.create_oval(100, 100, 140, 70, outline="blue", fill='green')
                 

	
def tester():
	texte.insert(Tkinter.END,' Cool ')

def deplace_gauche():
	global xv,yv
	if xv>4:
		xv=xv-8
		can.coords(vaisseau1, xv, yv)

def deplace_droite():
	global xv,yv
	if xv<450:
		xv = xv+8
		can.coords(vaisseau1, xv, yv)
		
def tirer():
	global xm1,ym1,flag1
	if flag1==0:
		xm1 = xv+20	
		ym1= yv-10
		flag1=1
		timer_missile1.start()

	
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

xa = 40
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
timer_missile1 = MyTimer(1,gestion_missile1)

# Créer une fenêtre graphique fond noir
can = Canvas(fen, width =500, height =500, bg ='red')
can.pack(side =TOP, padx =50, pady =50)

# afficher les éléments graphiques (vaisseau, alien, missile)
vaisseau1 = can.create_image(xv, yv, image=image_vaisseau1, anchor=NW)
missile1 = can.create_image(origine_xm,origine_ym, image=image_missile1, anchor=NW)
alien1 = can.create_image(xa,ya, image=image_alien1, anchor=NW)

# Créer des boutons 
b2 = Button(fen, text ='     Initial      ', command =initialiser)
b2.pack(side =RIGHT, padx =10, pady =10)

b3 = Button(fen, text =' TESTER ', command =tester)
b3.pack(side =LEFT, padx =8, pady =3)

# Créer une zone pour du texte :
texte=Tkinter.Text(fen, width=70, height=2)
texte.insert(Tkinter.END,'Bonjour les amis ')
texte.pack(side=Tkinter.LEFT)

# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# Pour charger un son
winsound.PlaySound("intro.wav", winsound.SND_ASYNC)


fen.mainloop()
# fen.destroy()

