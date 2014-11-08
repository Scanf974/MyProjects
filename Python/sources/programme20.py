# -*- coding: utf-8 -*-
# Programme taupe - jardinier
# mise en oeuvre d'une pile
# B. HOAREAU Dec 2011

import random
from scipy import *


def affiche_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		
def remplir_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			nb = random.randint(0,10)
			t[y,x] = nb
			

def empiler(x,y):
	global index
	index = index + 1
	pile[index,0] = x
	pile[index,1] = y

def depiler():
	global index
	pile[index,0] = 0
	pile[index,1] = 0
	index = index - 1
	
		
def taupe(x1,y1):
	trou_fait = 0
	x= random.randint(0,x1)   
	y= random.randint(0,y1)
	if t[y,x] == 0:     # si pas de trou
		t[y,x] = 1		# on fait un trou
		empiler(x,y)	# on sauvegarde x et y dans la pile
		trou_fait = 1
	
	return trou_fait    # renvoi 1 si la taupe a pu faire un trou

def jardinier(x1,y1):
	trou_supprime = 0
	if index > 0:	# si on a au moins 1 trou
		x = pile[index,0]
		y = pile[index,1]
		t[y,x] = 0   # on rebouche le trou
		depiler()	 # on l'enlève de la pile
		trou_supprime =1
	
	return trou_supprime   # renvoi 1 si trou bien supprimé


t=zeros([8,10],int)   # t[y,x] y=8 et x=10                     
                                
t[0,] = [0,0,0,0,0,0,0,0,0,0]
t[1,] = [0,0,0,0,0,0,0,0,0,0]
t[2,] = [0,0,0,0,0,0,0,0,0,0]
t[3,] = [0,0,0,0,0,0,0,0,0,0]
t[4,] = [0,0,0,0,0,0,0,0,0,0]
t[5,] = [0,0,0,0,0,0,0,0,0,0]
t[6,] = [0,0,0,0,0,0,0,0,0,0]
t[7,] = [0,0,0,0,0,0,0,0,0,0]

pile=zeros([100,2],int)  # je crée ma pile 2 colonnes
						 # pour sauvegarder x dans pile[index,0]  
						 # et y dans pile[index,1]

index = 0
fin = 0

affiche_tableau(10,8)   # x=10 et y=8 
print

while fin == 0:
	touche = raw_input("Taupe:t   Jardinier:J  fin:f ")
	if touche == "f":
		fin = 1    # pour sortir programme
	if touche == "t":
		trou = taupe(10,8)
		if trou == 1:
			print
			affiche_tableau(10,8)
			print "nb de trou: ",index
		else:
			print "-- on est tombé sur un trou déja fait"
	if touche == "j":
		a = jardinier(10,8)
		if a == 1:
			print
			affiche_tableau(10,8)
			print "nb de trou: ",index
		else:
			print "-- tous les trous supprimés !"	





	





                              
