# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
import time
import winsound
import Tkinter
import threading


# Variables en fontion du bas
pxo = 00
py3 = 0.0025*pxo*pxo - 2*pxo  + 450						#->
py2 = int(py3)											#---> arondir le nombre
py1 = py3-py2											#->
if py1 > 0.5:											#->			
	py1>=py2+1											#->			
else:													#->			
	py1=py2												#->
pyo = py1




fen = Tk()
image_ab = PhotoImage(file='ab.gif')




# Créer une fenêtre graphique fond noir
can = Canvas(fen, width =1200, height =500, bg ='black')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques (vaisseau, alien, missile)
vaisseau1 = can.create_image(pxo, pyo, image=image_ab, anchor=NW)




fen.mainloop()
# fen.destroy()
