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
		pxp = 0.75/a														#VARIE				
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
a = 2																	#a = angle initial
pu = 0.0025																#pu = puissance initial
pxp = 0.375																#pxp = vitesse sur x initial


# Position bird en  bas
pxo = 0
pyo = 450				


#fenetre
fen = Tk()
fen.title("Angry Chicken")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace
timer_deplace = MyTimer(0.001,deplace)

# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1200, height =500, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques
image_ab = ImageTk.PhotoImage(file='img/ab.png')
ab = can.create_image(pxo, pyo, image=image_ab, anchor=NW)


# Création d'un bouton
b = Button(fen,text="Quitter",command=fen.quit)
b.pack()



# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# fen.destroy()
fen.mainloop()

