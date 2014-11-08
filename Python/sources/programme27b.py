# -*- coding: utf-8 -*-
# Programme labyrinthe (chat trouve souris)

import random
from scipy import *

def affiche_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print


def tester_souris(x,y):
	if t[y,x+1] == 3 or t[y,x-1] == 3 or t[y-1,x] == 3 or t[y+1,x] ==3:
		a = 1	# souris trouvée
		print
		print "--- souris trouvee ---"
	else:
		a = 0   # pas trouvée
	return a    # renvoie 1 si souris trouvée
	
		
def visite(x,y):
	global fin
	print
	affiche_tableau(10,8)
	a = raw_input("appuyer sur entree")
	
	if tester_souris(x,y) == 1:
		fin =1
	
	
	if t[y,x+1] == 0 and fin==0:	# case à droite du chat
		t[y,x+1] = 4
		visite(x+1,y)

	if t[y,x-1] == 0 and fin==0:   # case à gauche du chat
		t[y,x-1] = 4
		visite(x-1,y)
		
	if t[y+1,x] == 0 and fin==0:   # case en dessous (bas) du chat
		t[y+1,x] = 4
		visite(x,y+1)
	
	if t[y-1,x] == 0 and fin==0:   # case au dessus (haut) du chat
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


fin = 0
visite(1,6)   # position du chat





	





                              
