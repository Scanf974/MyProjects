# -*- coding: utf-8 -*-
# Programme Angry Chicken 

from scipy import *
from Tkinter import *
import time
import winsound
import Tkinter
import threading

xm = 50
ym = 30

fen = Tk()
ab = PhotoImage(file='ab.gif')

# Créer une fenêtre graphique 

can = Canvas(fen,width=1200,height=500, bg ='Black')
can.pack(side =TOP, padx =50, pady =20)



# Création d'un bouton
b = Button(fen,text="Quitter",command=fen.quit)
b.pack()

# Pour charger un son
winsound.PlaySound("intro.wav", winsound.SND_ASYNC)

fen.mainloop()

# afficher les éléments graphiques (vaisseau, alien, missile)
bird1 = can.create_image(xm,ym, image=ab, anchor=NW)

