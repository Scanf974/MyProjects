# -*- coding: utf-8 -*-


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
        
        
def deplace():
	global a,pu,pxo,pyo,flag1
	
	if flag1==1:
		if pxo<1200 and pyo<450:								
			pxo = pxo + 10
			py3 = pu*pxo*pxo - a*pxo  + 450							#->
			py2 = int(py3)												#---> arondir le nombre
			py1 = py3-py2												#->
			if py1 > 0.5:												#->			
				py1>=py2+1												#->			
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
	global a,pu
	
	if evt.char=="t":
		tirer()
		
	if evt.char=="8":
		a = a + 0.1
				
	if evt.char=="5":
		a = a - 0.1

		
	if evt.char=="4":
		pu = pu + 0.0001
		
	if evt.char=="6":
		pu = pu - 0.0001





#Programme principal



#le flag1 c'est pour "autorisé" le lancement
flag1 = 0
a = 2
pu = 0.0025



# Position bird en  bas
pxo = 0
pyo = 450					


#fenetre et images
fen = Tk()
image_ab = PhotoImage(file='ab.gif')




#Timer de la fonction deplace
timer_deplace = MyTimer(0.015,deplace)

# Créer une fenêtre graphique fond noir
can = Canvas(fen, width =1200, height =500, bg ='black')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques (vaisseau, alien, missile)
ab = can.create_image(pxo, pyo, image=image_ab, anchor=NW)


# Création d'un bouton
b = Button(fen,text="Quitter",command=fen.quit)
b.pack()



# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

fen.mainloop()
# fen.destroy()
