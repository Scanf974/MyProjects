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

	
	
def teste_col(y,x):
	global pxd,pyd
	if flag1==1:
		if x>pxd and x<pxd+64 and y>pyd and y<pyd+64  or  x+60>pxd and x+60<pxd+64 and y+60>pyd and y+60<pyd+64:     #pour le 2 coins du birds
			can.delete(mac)
				


			
def deplace():
	global px,py,vx0,vy0,px0,py0,tps,flag1	
	if flag1 == 1:
		
		if px < 1200 and py < 482:			
			tps = tps + 0.01
			px = vx0*tps + px0
			py = (m*g)/2*tps*tps - vy0*tps + py0						
			can.coords(ab, px, py)
			teste_col(py,px)			
								
		else:			
			can.coords(ab, 0 , 300)										# revien pos initial	
			flag1=0
			timer_deplace.stop()
				
							
	
def tirer():
	global px,py,tps,flag1
	if flag1==0:
		tps = 0
		px = 0															#ici je ne sais pas pk, sinon ca marche pas
		py = 0															#ici
		flag1=1								
		timer_deplace.start()							



def affiche(evt):
	global angd,v0,vx0,vy0
	
	if evt.char=="t":
		tirer()

		
	if evt.char=="4":
		v0 = v0 - 4
		angr = 0.0174*angd
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
				
	if evt.char=="6":
		v0 = v0 + 4
		angr = 0.0174*angd
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		
	if evt.char=="8":													
		angd = angd + 3	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0	
																
	if evt.char=="5":
		angd = angd - 3	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0







###########################################################Programme principal###########################################################



#le flag1 c'est pour "autorisé" le lancement
flag1 = 0


# Conditions Initiale (Birds)
g = 9.81			#N/Kg
m = 1 				#KILOS
angd = 40.0			#DEGRES
angr = 0.0174*angd	#RADIAN
v0 = 80.0			#.../seconde
vx0 = cos(angr)*v0	#.../seconde
vy0 = sin(angr)*v0	#.../seconde
		
tps = 0				#seconde
px0 = 0				#position initiale sur x
py0 = 300			#position initiale sur y

pxd = 700
pyd = 300			


#fenetre
fen = Tk()
fen.title("Angry Chicken")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace
timer_deplace = MyTimer(0.001,deplace)


# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques
image_ld = ImageTk.PhotoImage(file='img/Loading.gif')						#le fond
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
mac = can.create_image(pxd, pyd, image=image_mac, anchor=NW)

image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(px0, py0, image=image_ab, anchor=NW)




# Création d'un bouton
b = Button(fen,text="Quitter",command=fen.quit,)
b.pack()



# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# fen.destroy()
fen.mainloop()

