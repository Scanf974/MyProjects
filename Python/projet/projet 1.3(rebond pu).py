# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
import time
import winsound
import Tkinter
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
			
def teste_sol(y,x):
	global pyo,pxo,pu,a
	if flag1==1:
		if pyo>=482:
			py3 =  pu*pxo*pxo - 2.5*a*pxo + 482 + 6/pu			#->
			py2 = int(py3)												#---> arondir le nombre
			py1 = py3-py2												#->
			if py1 > 0.5:												#->			
				py1=py2+1												#->			
			else:														#->			
				py1=py2													#->
			pyo = py1
			can.coords(ab, pxo, pyo)		
			
			
def deplace():
	global a,pu,pxp,pxo,pyo,flag1
	
	if flag1==1:
	
		if pxo<1200 and pyo<482:								
			pxo = pxo + pxp
			py3 = pu*pxo*pxo - a*pxo  + 450								#->
			py2 = int(py3)												#---> arondir le nombre
			py1 = py3-py2												#->
			if py1 > 0.5:												#->			
				py1=py2+1												#->			
			else:														#->			
				py1=py2													#->
			pyo = py1
			can.coords(ab, pxo, pyo)
			teste_col(pyo, pxo)
			teste_sol(pyo,pxo)
								
		else:
			
			can.coords(ab, 0 , 450)										# revien pos initial	
			flag1=0
			timer_deplace.stop()
		
	
			
	
def tirer():
	global pxo,pyo,flag1
	if flag1==0:
		pxo = 0															#ici je ne sais pas pk, sinon ca marche pas
		pyo= 0															#ici
		flag1=1								
		timer_deplace.start()


def affiche(evt):
	global a,pu,pxp
	
	if evt.char=="t":
		tirer()
		
	if evt.char=="8":													#Fonction inverse 1/x
		a = a + 0.1														#pour que la vitesse celon x
		pxp = 0.75/a													#VARIE				
	if evt.char=="5":
		a = a - 0.1
		pxp = 0.75/a
		
	if evt.char=="4":
		pu = pu + 0.0001		
	if evt.char=="6":
		pu = pu - 0.0001






###########################################################Programme principal###########################################################



#le flag1 c'est pour "autorisé" le lancement
flag1 = 0
a = 2.0																	#a = angle initial
pu = 0.0025																#pu = puissance initial
pxp = 0.375																#pxp = vitesse sur x initial


# Position bird en  bas
pxo = 0
pyo = 450

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
image_ld = ImageTk.PhotoImage(file='img/Loading.gif')						
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(pxo, pyo, image=image_ab, anchor=NW)


image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
mac = can.create_image(pxd, pyd, image=image_mac, anchor=NW)

# Création d'un bouton
b = Button(fen,text="Quitter",command=fen.quit)
b.pack()



# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# fen.destroy()
fen.mainloop()

