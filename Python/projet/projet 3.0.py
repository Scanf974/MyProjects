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
	if flag1<>0:
		if x>pg.x and x<pg.x+64 and y>pg.y and y<pg.y+64  or x+60>pg.x and x<pg.x+64 and y>pg.y and y<pg.y+64  or x>pg.x and x+606<pg.x+64 and y>pg.y and y<pg.y+64  or  x+60>pg.x and x+60<pg.x+64 and y+60>pg.y and y+60<pg.y+64:     #pour le 4 coins du birds
			can.delete(mac)
	
	
class CondInit:
	"conditions initialles"
	def __init__(self):
		self.g = 9.81			#N/Kg
		self.m = 1 				#KILOS
		self.angd = 40.0			#DEGRES
		self.angr = 0.0174*self.angd 	#RADIAN
		self.v0 = 80.0			#.../seconde
		self.vx0 = cos(self.angr)*self.v0	#.../seconde
		self.vy0 = sin(self.angr)*self.v0	#.../seconde
		self.tps = 0		

class PosInit(CondInit):
	"pos init du squirel"		
	def __init__(self, x0 = 0, y0 = 340):
		self.x0 = x0				#position initiale sur x
		self.y0 = y0			#position initiale sur y
					
	
class Deplace(PosInit):
	"pour l'ecureuil"
	
	def __init__(self):
		self.x = 0
		self.y = 340
			
	def deplace(self):			
				
		if self.x < 1200 and self.y > 340:
			x0 = x
			y0 = 340
						
			v1 = v0 * 0.2										#.../seconde			
			angd = angd
			angr = 0.0174*angd											#0 a 1.5 RADIAN
			vx0 = cos(angr)*v1
			vy0 = sin(angr)*v1
			if v1 < 1:
				stop()
				
			self.tps = 0			
			self.tps = self.tps + 0.01
			x = vx0*self.tps + x0
			y = (m*g)/2*self.tps*self.tps - vy0*self.tps + y0								
			
								
		elif px < 1200 and py < 482:			
			self.tps = self.tps + 0.01
			x = vx0*self.tps + x0
			y = (m*g)/2*self.tps*self.tps - vy0*self.tps + y0						
										
				
		else:			
			stop()
				
		can.coords(ab, x, y)
		teste_col(y,x)		
						

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
	
	if evt.char=="y":
		pg.objet()
	
	if evt.char=="g":
		stop()


class Objet:
	"les glands"
	
	def __init__(self, x = 500, y = 200):
		self.x = x
		self.y = y
		
		
	def objet(self):
		
		pg.y = random.randint(200,327)	
		pg.x = random.randint(700,1000)								
		mac = can.create_image(pg.x, pg.y, image=image_mac, anchor=NW)
		


def tirer():
	global px,py,tps,flag1,fum
	if flag1==0:
		tps = 0
		px = 0															#ici je ne sais pas pk, sinon ca marche pas
		py = 0															#ici
		flag1=1								
		timer_deplace.start()


def stop():
	global px0,py0,angr,angd,v0,vx0,vy0,flag1,ab
	
	timer_deplace.stop()
	can.coords(ab, 0 , 340)										# revien pos initial	
	px0 = 0
	py0 = 340
	angd = angd
	angr = 0.0174*angd
	v0 = v0
	vx0 = cos(angr)*v0	#.../seconde
	vy0 = sin(angr)*v0	#.../seconde
	flag1=0								#les birds
							



###########################################################Programme principal###########################################################



#le flag1 c'est pour "autorisé" le lancement
flag1 = 0


# Conditions Initiale (Birds)
c = CondInit()


ps = PosInit()
ps.d = Deplace()



pg = Objet()
pg.y = random.randint(200,327)	
pg.x = random.randint(700,1000)			




#fenetre
fen = Tk()
fen.title("Angry Chicken")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace

timer_trace = MyTimer(0.1,trace)
timer_deplace = MyTimer(0.01,ps.d.deplace)


# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques
image_ld = ImageTk.PhotoImage(file='img/Loading.gif')						#le fond
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_sol = ImageTk.PhotoImage(file='img/bg2.png')						#le fond
sol = can.create_image(0, 351, image=image_sol, anchor=NW)


image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
mac = can.create_image(pg.x, pg.y, image=image_mac, anchor=NW)


image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(ps.x0, ps.y0, image=image_ab, anchor=NW)




# Création d'un bouton
b1 = Button(fen,text="Quitter",command=fen.quit,)
b1.pack(side =LEFT, padx =3, pady =3)




# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)

# fen.destroy()
fen.mainloop()

