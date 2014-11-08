# -*- coding: utf-8 -*-
# BallSquirrel 2.5 (sans les graphisques)
# Sautron Bruno, Maillot Paul, Bijoux Hugo

from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk
import os


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
	global pxg,pyg,points,nbg,pt
	if (x>pxg and x<(pxg+64) and y>pyg and y<(pyg+64))  or ((x+60)>pxg and x<(pxg+64) and y>pyg and y<(pyg+64))  or (x>pxg and x<(pxg+64) and y>pyg and y<(pyg+64))  or  ((x+60)>pxg and (x+60)<(pxg+64) and (y+60)>pyg and (y+60)<(pyg+64)):     #pour le 4 coins du birds
		can.delete(mac)
		stop3()
		
		points = points + pt
		print "Touche!  + " ,pt,
		print ":" ,points
		
	
def teste_col2(y,x):
	global pxg2,pyg2,points,nbg,pt
	if (x>pxg2 and x<(pxg2+64) and y>pyg2 and y<(pyg2+64))  or ((x+60)>pxg2 and x<(pxg2+64) and y>pyg2 and y<(pyg2+64))  or (x>pxg2 and x<(pxg2+64) and y>pyg2 and y<(pyg2+64))  or  ((x+60)>pxg2 and (x+60)<(pxg2+64) and (y+60)>pyg2 and (y+60)<(pyg2+64)):     #pour le 4 coins du birds
		can.delete(mac2)
		stop3_2()
		points = points + pt
		print "Touche!  + " ,pt,
		print ":" ,points
		
		

def latd():
	global px0,py0,lx,ly
	
	if flag1 == 0:
		lx = lx + 20
		
	if lx >= 700:
		lx = 700		
	pos_bird()
	
		
def latg():
	global px0,py0,lx,ly
	
	if flag1 == 0:
		lx = lx - 20
		
	if lx <= -20:
		lx = -20		
	pos_bird()


def deplace_gland():
	global pxg0,pyg0,tpg,vg0,anggd,anggr,vxg0,vyg0,pxg,pyg,nbg,lvl,points,pt,mac
	
	
	if pxg < 1200 and pyg < 326:		
		tpg = tpg + 0.05
		pxg = vxg0*tpg + pxg0
		pyg = (m*g)/2*tpg*tpg - vyg0*tpg + pyg0						
		
	else:
		can.delete(mac)
		stop3()
		
		points = points - (pt/2)
		print "Aaaarg -" ,pt/2,
		print ": " ,points
					
	can.coords(mac, pxg, pyg)							
			

def deplace_gland2():
	global pxg0,pyg0,tpg2,vg02,anggd2,anggr2,vxg02,vyg02,pxg2,pyg2,nbg,lvl,points,pt,mac2,p2
	
	
	if pxg2 < 1200 and pyg2 < 326:		
		tpg2 = tpg2 + 0.05
		pxg2 = vxg02*tpg2 + pxg0 
		pyg2 = (m*g)/2*tpg2*tpg2 - vyg02*tpg2 + (pyg0-p2)						
		
	else:
		
		can.delete(mac2)
		stop3_2()
		
		points = points - (pt/2)
		print "Aaaarg -" ,pt/2,
		print ": " ,points
					
	can.coords(mac2, pxg2, pyg2)								
			
def deplace():
	global px,py,vx0,vy0,px0,py0,tps,flag1,angd,angr,v0,v1,e,lx,ly,lvl
	
	teste_col(py,px)
	if lvl >=10:
		teste_col2(py,px)

	if flag1 <> 0:
	
		if px > -20 and px < 900:			
		
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
				tps = tps + 0.10
				px = vx0*tps + px0
				py = (m*g)/2*tps*tps - vy0*tps + py0								
				

		
								
			elif px < 1200 or px < 482:
								
				tps = tps + 0.10
				px = vx0*tps + px0
				py = (m*g)/2*tps*tps - vy0*tps + py0						
									
				
			else:			
				stop2()
				pos_bird()
				
			can.coords(ab, px, py)
	
		else:
			stop2()
			pos_bird()	
			
						


def affiche(evt):
	global angd,v0,vx0,vy0,px0,py0
	
	if evt.char==" ":
		tirer()
		
	if evt.char=="s":
		v0 = v0 - 8
		if v0 < 30:														#vitesse MIN
			v0 = 30.0
		angr = 0.0174*angd
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		pos_bird()
				
	if evt.char=="z":
		v0 = v0 + 8
		if v0 > 75:													#vitesse MAX
			v0 = 75.0
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
		if angd <= 60:													#angle MIN
			angd = 60	
		angr = 0.0174*angd													#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0		
		latd()
		
		
	if evt.char == "q":	
		angd = angd + 2
		if angd >= 120:													#angle MIN
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
	global image_mac,mac,pyg0,pxg0
	
	pyg0 = random.randint(200,327)	
	pxg0 = random.randint(700,1000)
	
	image_mac = ImageTk.PhotoImage(file='img/mac.png')							
	mac = can.create_image(pxg0, pyg0, image=image_mac, anchor=NW)


def tire_gland():
	global pxg,pyg,tpg,image_mac,mac,vg0,anggd,anggr,vxg0,vyg0,nbg,lvl,pxg0,pyg0
	image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
	mac = can.create_image(pxg0, pyg0, image=image_mac, anchor=NW)	
	
	
	tpg = 0	
	anggd = random.randint(130,150)			#DEGRES
	anggr = 0.0174*anggd					#RADIAN
	vg0 = random.randint(80.0,90.0+lvl)		#pixels/seconde
	vxg0 = cos(anggr)*vg0					#pixels/seconde
	vyg0 = sin(anggr)*vg0					#pixels/seconde
	pxg = pxg0
	pyg = pyg0
	
	
	nbg = nbg +1
	print nbg,
	print 
	
	timer_deplace_gland.start()
	
		

def tire_gland2():
	global pxg2,pyg2,tpg2,image_mac2,mac2,vg02,anggd2,anggr2,vxg02,vyg02,nbg,lvl,pxg0,pyg0,p2
	image_mac2 = ImageTk.PhotoImage(file='img/mac2.png')							#les dechets
	mac2 = can.create_image(pxg0, pyg0-p2, image=image_mac2, anchor=NW)	
	
	
	tpg2 = 0	
	anggd2 = random.randint(110,165)		#DEGRES
	anggr2 = 0.0174*anggd2					#RADIAN
	vg02 = random.randint(65.0,75.0)	#pixels/seconde
	vxg02 = cos(anggr2)*vg02					#pixels/seconde
	vyg02 = sin(anggr2)*vg02					#pixels/seconde
	pxg2 = pxg0
	pyg2 = pyg0 - p2
	nbg = nbg +1
	print nbg,
	print 
	
	timer_deplace_gland2.start()
	
		
		


def tirer(x,y):
	global px,py,tps,flag1,image_fum,fum,v1,v0,angr,angd,vx0,vy0
	
	can.delete(f1)
	can.delete(f2)
	can.delete(f3)
	can.delete(f4)
	
	if flag1 == 0:
		
		oppose = py0 + 30 - y	
			
		if x < px0+30:
		
			adjacent = px0+30 - x
			tanj = oppose/adjacent
			angd = 180 - math.degrees(math.atan(tanj))
			if angd < 90:
				angd = 90
	
			angr = 0.0174*angd	
			h = adjacent/cos(angr)*-1								#cosinus negatif


		
			
		elif x > px0+30:
					
			adjacent = x - px0+30
			tanj = oppose/adjacent
			angd = math.degrees(math.atan(tanj))
			if angd > 90:
				angd = 90
			
				
			angr = 0.0174*angd
			h = adjacent/cos(angr)

			
		else:
			angd = 90
			print oppose,adjacent,angd
			angr = 0.0174*angd													#0 a 1.5 RADIAN
		
			
		v0 = h*0.2	
		if v0 >= 80:
			v0 = 80												#0 a 1.5 RADIAN
		vx0 = cos(angr)*v0
		vy0 = sin(angr)*v0
		
		
	
		
		os.system("cls")	
			
	
		print "Angle=",int(angd)
		print "v0=",int(v0)
		
		
		
		image_fum = ImageTk.PhotoImage(file='img/fum.png')					#permet d'effacer les anciennes traces
		v1 = v0
		tps = 0
		px = 0															#ici je ne sais pas pk, sinon ca marche pas
		py = 0															#ici
		flag1=1							
		timer_deplace.start()
		timer_trace.start()
		

		
			
def niveau():
	global vg0,vxg0,vyg0,lvl,pt
	
	lvl = lvl + 1
	pt = 5*lvl
	
	if lvl == 9:
		timer_gland2.start()	
	


def stop1():
	global px0,py0,angr,angd,v0,v1,vx0,vy0,flag1,ab,ly,lx				#Stop normal
	timer_deplace.stop()
	timer_trace.stop()
	lx = px
	ly = py
	can.coords(ab, lx , ly)												# reste mm position		
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
	can.coords(ab, px0 , py0)											# revien pos initial		
	angd = angd
	angr = 0.0174*angd
	v0 = v0
	vx0 = cos(angr)*v0	#.../seconde
	vy0 = sin(angr)*v0	#.../seconde
	flag1=0								
	
def stop3():
	
	global pxg,pyg,tpg,image_mac,mac,vg0,anggd,anggr,vxg0,vyg0
	timer_deplace_gland.stop()
	
	tpg = 0	
	anggd = 0		#DEGRES
	anggr = 0					#RADIAN
	vg0 = 0		#pixels/seconde
	vxg0 = 0					#pixels/seconde
	vyg0 = 0					#pixels/seconde
	pxg = 0
	pyg = 0
	
						
def stop3_2():
	
	global pxg2,pyg2,tpg2,image_mac2,mac2,vg02,anggd2,anggr2,vxg02,vyg02
	timer_deplace_gland2.stop()
	
	tpg2 = 0	
	anggd2 = 0		#DEGRES
	anggr2 = 0					#RADIAN
	vg02 = 0		#pixels/seconde
	vxg02 = 0					#pixels/seconde
	vyg02 = 0					#pixels/seconde
	pxg2 = 0
	pyg2 = 0
	
						
		
def trace():
	global ab1,px,py,image_fum,fum

	fum = can.create_image(px+30, py+30, image=image_fum, anchor=NW)
	

def boot():
	global image_logo,logo,bt
		
	if bt >= 0:
		can.delete(logo)
		timer_boot.stop()
		timer_gland.start()
		timer_niveau.start()
		timer_temps.start()
	
def pause():
	global paus
	paus = paus + 1
	if paus == 1:
		if flag1 <> 0:		
			timer_deplace.stop()	
		timer_deplace_gland.stop()	
		timer_deplace_gland2.stop()
	if paus == 2:
		paus = 0
	if paus == 0:
		timer_deplace.start()	
		timer_deplace_gland.start()	
		timer_deplace_gland2.start()		
		

def pointeur(event):
    x,y = event.x,event.y #une instance d'une classe qui fournit les coordonnées du clic dans le canvas
                          #par le biais de ses attributs x et y (le nom event est donné à l'argument
                          #conventionnellement
  
    tirer(x,y)
 
 
def temps():
	global ts,tm
	ts = ts + 1
	if ts >= 60:
		ts = 0
		tm = tm + 1
	chaine.configure(text = str(tm) + ":" + str(ts) )

###########################################################Programme principal###########################################################



#le flag1 c'est pour "autorisé" le lancement

paus = 0
flag1 = 0
points=0
nbg = 0
lvl = 1
pt = 50
bt = 1
ts = 0
tm = 0

tps = 0				#(pour squirrel) second
tpg = 0				#(pour gland) seconde
g = 9.81			#N/Kg
m = 1 				#KILOS

# Conditions Initiale (Squirrel)
angd = 85.0			#DEGRES
angr = 0.0174*angd	#RADIAN
v0 = 70.0			#pixels/seconde
vx0 = cos(angr)*v0	#pixels/seconde
vy0 = sin(angr)*v0	#pixels/seconde
v1 = v0

lx = 100				#c'était pour le lanceur d'avant ^^
ly = 340				#c'était pour le lanceur d'avant ^^
px0 = lx				#position initiale sur x
py0 = ly				#position initiale sur y

e = 0.3					#coefficient de rebond du squirrel


#position initiale (GlandS)
pyg0 = 300	
pxg0 = 1100

p2 = 200

#fenetre
fen = Tk()
fen.title("BallSquirrel")												
frame = Frame(fen)
frame.pack()



#Timer de la fonction deplace
timer_deplace = MyTimer(0.01,deplace)
timer_deplace_gland = MyTimer(0.01,deplace_gland)
timer_deplace_gland2 = MyTimer(0.01,deplace_gland2)
timer_trace = MyTimer(0.06,trace)
timer_niveau = MyTimer(8.0,niveau)
timer_gland = MyTimer(6.0,tire_gland)
timer_gland2 = MyTimer(7.86,tire_gland2)
timer_boot = MyTimer(5.0,boot)
timer_temps = MyTimer(1.0,temps)


# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.bind("<Button-1>", pointeur)
can.pack(side =TOP, padx =0, pady =0)

# afficher les éléments graphiques
image_ld = ImageTk.PhotoImage(file='img/decors.png')						#le fond
ld = can.create_image(0, 0, image=image_ld, anchor=NW)

image_sol = ImageTk.PhotoImage(file='img/bg2.png')							#le sol
sol = can.create_image(0, 351, image=image_sol, anchor=NW)

image_mac = ImageTk.PhotoImage(file='img/mac.png')							#les dechets
mac = can.create_image(pxg0, pyg0, image=image_mac, anchor=NW)
image_mac2 = ImageTk.PhotoImage(file='img/mac2.png')							#les dechets
mac2 = can.create_image(pxg0, pyg0-p2, image=image_mac2, anchor=NW)


image_fum2 = ImageTk.PhotoImage(file='img/fum2.png')							#les birds
f1 = can.create_image(lx+vx0*0.00+30, ly-vy0*0.00+30, image=image_fum2, anchor=NW)
f2 = can.create_image(lx+vx0*0.25+30, ly-vy0*0.25+30, image=image_fum2, anchor=NW)
f3 = can.create_image(lx+vx0*0.50+30, ly-vy0*0.50+30, image=image_fum2, anchor=NW)
f4 = can.create_image(lx+vx0*0.75+30, ly-vy0*0.75+30, image=image_fum2, anchor=NW)

image_ab = ImageTk.PhotoImage(file='img/ab.png')							#les birds
ab = can.create_image(px0, py0, image=image_ab, anchor=NW)

image_logo = ImageTk.PhotoImage(file='img/logo.png')							
logo = can.create_image(200, -50, image=image_logo, anchor=NW)




timer_boot.start()



# Création d'un bouton
b1 = Button(fen,text="Quitter",command=fen.quit,)
b1.pack(side =LEFT, padx =3, pady =3)

b2 = Button(fen,text="Pause/Play",command=pause,)
b2.pack(side =LEFT, padx =3, pady =3)


chaine = Label(fen)
chaine.pack()


instruction=Label(fen, text="Cliquez pour lancer!!!!!",fg='black') 
instruction.pack()





# Pour la gestion du clavier 
fen.bind_all('<Key>', affiche)


# fen.destroy()
fen.mainloop()

