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
	if flag1<>0:
		if x>pxd and x<pxd+64 and y>pyd and y<pyd+64  or x+60>pxd and x<pxd+64 and y>pyd and y<pyd+64  or x>pxd and x<pxd+64 and y>pyd and y<pyd+64  or  x+60>pxd and x+60<pxd+64 and y+60>pyd and y+60<pyd+64:     #pour le 4 coins du birds
			can.delete(mac)

def latd():
	global px0,py0,lx,ly
	
	if flag1 == 0:
		lx = lx + 20
		
	if lx >= 900:
		lx = 900		
	pos_bird()
	
		
def latg():
	global px0,py0,lx,ly
	
	if flag1 == 0:
		lx = lx - 20
		
	if lx <= -20:
		lx = -20		
	pos_bird()
	
		



def deplace_avant():
	 #Ca serra pour les glands plutard
		
	if flag1 <> 0:
		
		if px < lx or py > ly:
		
			tps = tps + 0.01
			px = vx0*tps + px0
			py = -vy0*tps + py0
			
													
		else:	
			timer_deplace_avant.stop()
			timer_deplace.start()
			timer_trace.start()
			pos_bird()

	can.coords(ab, px, py)
	can.coords(f1, vx0*0.00*tps + (lx-vx0*0.00+30) ,-vy0*0.00*tps+ (ly+vy0*0.00+30))	
	can.coords(f2, vx0*0.25*tps + (lx-vx0*0.25+30) ,-vy0*0.25*tps+ (ly+vy0*0.25+30))	
	can.coords(f3, vx0*0.50*tps + (lx-vx0*0.50+30) ,-vy0*0.50*tps+ (ly+vy0*0.50+30))	
	can.coords(f4, vx0*0.75*tps + (lx-vx0*0.75+30) ,-vy0*0.75*tps+ (ly+vy0*0.75+30))
	

			
def deplace():
	global px,py,vx0,vy0,px0,py0,tps,flag1,angd,angr,v0,v1,e,lx,ly
	
	if flag1 <> 0:
	
		if px > -20 and px < 1000:			
		
			if px < 1200 and py > 340:
				
				timer_trace.stop()
				px0 = px
				py0 = 340
				flag1=flag1+1			
				v1 = v1 * e													#.../seconde			
				angd = angd
				angr = 0.0174*angd											#0 a 1.5 RADIAN
				vx0 = cos(angr)*v1
				vy0 = sin(angr)*v1
				if v1 < 0.01:
					stop1()
					pos_bird()
				
				tps = 0			
				tps = tps + 0.01
				px = vx0*tps + px0
				py = (m*g)/2*tps*tps - vy0*tps + py0								
				

		
								
			elif px < 1200 or px < 482:
								
				tps = tps + 0.01
				px = vx0*tps + px0
				py = (m*g)/2*tps*tps - vy0*tps + py0						
									
				
			else:			
				stop2()
				pos_bird()
				
			can.coords(ab, px, py)
			teste_col(py,px)
	
		else:
			stop2()
			pos_bird()		
						

def affiche(evt):
	global angd,v0,vx0,vy0,px0,py0,vilat,vix,xiy,acc,tps
	
	if evt.char==" ":
		tirer()
		
	if evt.char=="s":
		v0 = v0 - 3
		if v0 < 20:														#vitesse MIN
			v0 = 20
		angr = 0.0174*angd
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		pos_bird()
				
	if evt.char=="z":
		v0 = v0 + 3
		if v0 > 104:													#vitesse MAX
			v0 = 104
		angr = 0.0174*angd
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		pos_bird()
		
	if evt.char=="a":													
		angd = angd + 8
		if angd > 120:													#angle MAX
			angd = 120
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		pos_bird()	
																
	if evt.char=="e":
		angd = angd - 8
		if angd < 60:													#angle MIN
			angd = 60	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		pos_bird()
		
	if evt.char == "d":
		angd = angd - 2
		if angd < 60:													#angle MIN
			angd = 60	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0		
		latd()
		
		
	if evt.char == "q":	
		angd = angd + 2
		if angd > 120:													#angle MIN
			angd = 120	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		latg()
		
	
	if evt.char=="y":
		objet()
	
	if evt.char=="g":
		stop2()
		pos_bird()


def pos_bird():
	global image_ab,ab,py0,px0,lx,ly,image_fum2,f1,f2,f3,f4,image_lanceur2,image_lanceur,lanceur2,lanceur

	px0 = lx	
	py0 = ly
	
	image_fum2 = ImageTk.PhotoImage(file='img/fum2.png')							#les birds
	f1 = can.create_image(lx+vx0*0.00+30, ly-vy0*0.00+30, image=image_fum2, anchor=NW)
	f2 = can.create_image(lx+vx0*0.25+30, ly-vy0*0.25+30, image=image_fum2, anchor=NW)
	f3 = can.create_image(lx+vx0*0.50+30, ly-vy0*0.50+30, image=image_fum2, anchor=NW)
	f4 = can.create_image(lx+vx0*0.75+30, ly-vy0*0.75+30, image=image_fum2, anchor=NW)	
		
	image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
	ab = can.create_image(px0, py0, image=image_ab, anchor=NW)
	

	
	
def objet():
	global image_mac,mac,pyd,pxd
	
	pyd = random.randint(200,327)	
	pxd = random.randint(700,1000)
	
	image_mac = ImageTk.PhotoImage(file='img/mac.png')							
	mac = can.create_image(pxd, pyd, image=image_mac, anchor=NW)


def tirer():
	global px,py,tps,flag1,image_fum,fum,v1,v0
	if flag1==0:
		image_fum = ImageTk.PhotoImage(file='img/fum.png')					#permet d'effacer les anciennes traces
		v1 = v0
		tps = 0
		px = 0															#ici je ne sais pas pk, sinon ca marche pas
		py = 0															#ici
		flag1=1							
		timer_deplace.start()
		timer_trace.start()	
			

							
	

def stop1():
	global px0,py0,angr,angd,v0,v1,vx0,vy0,flag1,ab,ly,lx				#Stop normal
	timer_deplace.stop()
	timer_trace.stop()
	lx = px
	ly = py
	can.coords(ab, 200-vx0 , 200+vy0)										# reste mm position		
	angd = angd
	angr = 0.0174*angd
	v0 = v0
	vx0 = cos(angr)*v0	#.../seconde
	vy0 = sin(angr)*v0	#.../seconde
	flag1=0							
	
def stop2():															# Stop quand sort limite		
	global px0,py0,angr,angd,v0,v1,vx0,vy0,flag1,ab
	timer_deplace.stop()
	timer_trace.stop()
	can.coords(ab, 200-vx0 , 200+vy0)										# revien pos initial		
	angd = angd
	angr = 0.0174*angd
	v0 = v0
	vx0 = cos(angr)*v0	#.../seconde
	vy0 = sin(angr)*v0	#.../seconde
	flag1=0	
							
		
def trace():
	global ab1,px,py,image_fum,fum

	fum = can.create_image(px+30, py+30, image=image_fum, anchor=NW)
	

###########################################################Programme principal###########################################################



#le flag1 c'est pour "autorisé" le lancement
flag1 = 0


# Conditions Initiale (Birds)
g = 9.81			#N/Kg
m = 1 				#KILOS
angd = 85.0			#DEGRES
angr = 0.0174*angd	#RADIAN
v0 = 80.0			#.../seconde
vx0 = cos(angr)*v0	#.../seconde
vy0 = sin(angr)*v0	#.../seconde
v1 = v0



e = 0.1				#coefficient de rebond du bird
		
tps = 0				#seconde


lx = 100				#position centre du lanceur
ly = 340				#position centre du lanceur
px0 = lx			#position initiale sur x
py0 = ly			#position initiale sur y

pyd = random.randint(200,327)	
pxd = random.randint(700,1000)			


#fenetre
fen = Tk()
fen.title("Angry Chicken")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace
timer_deplace_avant = MyTimer(0.001,deplace_avant)
timer_deplace = MyTimer(0.001,deplace)
timer_trace = MyTimer(0.06,trace)



# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques
image_ld = ImageTk.PhotoImage(file='img/Loading.gif')						#le fond
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_sol = ImageTk.PhotoImage(file='img/bg2.png')							#le sol
sol = can.create_image(0, 351, image=image_sol, anchor=NW)

image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
mac = can.create_image(pxd, pyd, image=image_mac, anchor=NW)


image_fum2 = ImageTk.PhotoImage(file='img/fum2.png')							#les birds
f1 = can.create_image(lx+vx0*0.00+30, ly-vy0*0.00+30, image=image_fum2, anchor=NW)
f2 = can.create_image(lx+vx0*0.25+30, ly-vy0*0.25+30, image=image_fum2, anchor=NW)
f3 = can.create_image(lx+vx0*0.50+30, ly-vy0*0.50+30, image=image_fum2, anchor=NW)
f4 = can.create_image(lx+vx0*0.75+30, ly-vy0*0.75+30, image=image_fum2, anchor=NW)

image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(px0, py0, image=image_ab, anchor=NW)






# Création d'un bouton
b1 = Button(fen,text="Quitter",command=fen.quit,)
b1.pack(side =LEFT, padx =3, pady =3)

b2 = Button(fen,text="+Objet",command=objet,)
b2.pack(side =LEFT, padx =3, pady =3)



# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)


# fen.destroy()
fen.mainloop()

