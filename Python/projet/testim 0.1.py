# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
import time
import winsound
import Tkinter
import threading


# Variables du vaisseau
xv = 100
yv = 400


fen = Tk()
image_ab = PhotoImage(file='ab.gif')




# Créer une fenêtre graphique fond noir
can = Canvas(fen, width =1200, height =500, bg ='Black')
can.pack(side =TOP, padx =50, pady =20)

# afficher les éléments graphiques (vaisseau, alien, missile)
vaisseau1 = can.create_image(xv, yv, image=image_ab, anchor=NW)




fen.mainloop()
# fen.destroy()
