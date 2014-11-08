# -*- coding: utf-8 -*-

from Tkinter import *
 
def pointeur(event):
	
	
    x,y = event.x,event.y #une instance d'une classe qui fournit les coordonnées du clic dans le canvas
                          #par le biais de ses attributs x et y (le nom event est donné à l'argument
                          #conventionnellement
                          
    chaine.configure(text = "Clic détecté en X =" + str(x) +", Y =" + str(y))
    
 
fen = Tk()

can = Canvas(fen, width =1200, height =500, bg="light yellow")
can.bind("<Button-1>", pointeur) #on lie le clic gauche à la fonction "rond"
can.pack()

chaine = Label(fen)
chaine.pack()
 
fen.mainloop()
