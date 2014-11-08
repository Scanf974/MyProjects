
# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk


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
	


	
def moov():	
	global py,py0
	py = (m*g)/2*tps*tps - vy0*tps + py0	
													
			
def deplace():
	global py,tps			
	tps = tps + 0.14
	moov()
	can.coords(ab, 0, py)
	
	
def deplace_sol():
	global psolx,sol,sol2,image_sol
	
	
	if psolx <= -1198:	
		can.delete(sol)
		can.delete(sol2)			
		psolx = 0			
		sol = can.create_image(psolx, 351, image=image_sol, anchor=NW)
		sol2 = can.create_image(psolx + 1200, 351, image=image_sol, anchor=NW)


		
	psolx = psolx - 5
	can.coords(sol, psolx, 351)
	can.coords(sol2, psolx+1198, 351)
								

def tirer():
	global flag,angr,angd,v0,vy0,py0,tps
	
		
	if flag == 0:
		angd = 90		#DEGRES
		angr = 0.0174*angd	#RADIAN
		v0 = 50.0			#pixels/seconde
		vy0 = sin(angr)*v0
		tps = 0
		
		py0 = py
		
		flag = 1							
		timer_deplace.start()
		
		
def affiche(evt):
	global flag
	
	if evt.char==" ":
		if flag == 1:
			timer_deplace.stop()
			flag = 0
		tirer()
	
	
###########################################################Programme principal###########################################################

flag = 0

px0 = 0
py0 = 300
py = py0

g = 12.81			#N/Kg
m = 1 				#KILOS

psolx = 0

# Conditions Initiale (Squirrel)
tps = 0
angd = 90			#DEGRES
angr = 0.0174*angd	#RADIAN
v0 = 0				#pixels/seconde
vy0 = sin(angr)*v0	#pixels/seconde


#fenetre
fen = Tk()
fen.title("Flapy Birds")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace
timer_deplace = MyTimer(0.01,deplace)
timer_sol = MyTimer(0.05,deplace_sol)




# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques
image_ld = ImageTk.PhotoImage(file='img/decors.png')						#le fond
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_sol = ImageTk.PhotoImage(file='img/bg2.png')							#le sol
sol = can.create_image(psolx, 351, image=image_sol, anchor=NW)							
sol2 = can.create_image(1198, 351, image=image_sol, anchor=NW)


image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(px0, py0, image=image_ab, anchor=NW)




# Création d'un bouton
b1 = Button(fen,text="Quitter",command=fen.quit,)
b1.pack(side =LEFT, padx =3, pady =3)



timer_sol.start()

# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# fen.destroy()
fen.mainloop()

