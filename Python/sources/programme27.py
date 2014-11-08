# -*- coding: utf-8 -*-
# Programme labyrinthe (chat souris)

import random
from scipy import *

def affiche_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		
def visite(x,y):
	
	print
	affiche_tableau(10,8)
	a = raw_input("appuyer sur entree")
	
	if t[y,x+1] == 0:	# case à droite du chat
		t[y,x+1] = 4
		visite(x+1,y)

	if t[y,x-1] == 0:   # case à gauche du chat
		t[y,x-1] = 4
		visite(x-1,y)
		
	if t[y+1,x] == 0:   # case en dessous (bas) du chat
		t[y+1,x] = 4
		visite(x,y+1)
	
	if t[y-1,x] == 0:   # case au dessus (haut) du chat
		t[y-1,x] = 4
		visite(x,y-1)
		
		
	

t=zeros([8,10],int)   # t[y,x] y=8 et x=10                     
                                
t[0,] = [1,1,1,1,1,1,1,1,1,1]
t[1,] = [1,0,0,0,0,0,1,0,0,1]
t[2,] = [1,0,1,1,1,1,1,0,0,1]
t[3,] = [1,0,0,0,1,0,0,0,0,1]
t[4,] = [1,0,0,0,1,0,0,0,3,1]
t[5,] = [1,0,0,0,0,0,1,1,1,1]
t[6,] = [1,2,0,0,0,0,0,0,0,1]
t[7,] = [1,1,1,1,1,1,1,1,1,1]


visite(1,6)   # position du chat





	





                              
