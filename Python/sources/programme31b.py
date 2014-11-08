# -*- coding: utf-8 -*-
# Programme Morpion
# Version humain contre ordinateur

import random
from scipy import *

def affiche_tableau(x1,y1):
	print
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print

def aligner(n):
	res = 0		

	for i in range(3):   # test des lignes
		if t[i,0] == n and t[i,1] == n and t[i,2] == n:
			res =1
	
	for i in range(3):   # test des colonnes
		if t[0,i] == n and t[1,i] == n and t[2,i] == n:
			res =1

	# test des diagonales :	
	if t[0,0] == n and t[1,1] == n and t[2,2] == n:
		res =1
			
	if t[2,0] == n and t[1,1] == n and t[0,2] == n:
		res = 1
			
	return res

def joueur1():
	
	ok = 0
	while ok==0:
		x,y = input("JOUEUR 1 : entrer x , y :")	
		if t[y,x] ==0:
			t[y,x] = 1
			ok = 1
		else:
			print "erreur, recommencer"
			

def ordinateur():
	x= -1
	y= -1
	milieu = 0
	gagne = 0
	while x<2 and gagne==0:
		x= x+1
		y= -1
		while y<2 and gagne==0:
			y=y+1
			if t[y,x] ==0:
				t[y,x] = 2
				if aligner(2) == 1:
					gagne = 1
				else:
					t[y,x] = 0
	
						# faut jouer un coup
						# on va jouer pour bloquer
	if gagne ==0:		# coup gagnant de l'adversaire
		x= -1			# on simule coup adversaire
		y= -1
		milieu = 0
		gagne_humain = 0
		while x<2 and gagne_humain==0:
			x= x+1
			y= -1
			while y<2 and gagne_humain==0:
				y=y+1
				if t[y,x] ==0:
					t[y,x] = 1
					if aligner(1) == 1:
						gagne_humain  = 1
						x_save = x
						y_save = y
					else:
						x_defaut = x
						y_defaut = y
						
					t[y,x] = 0			
					
		if gagne_humain == 1:		# on bloque coup gagnant adverse
			t[y_save,x_save] = 2
		elif t[1,1] == 0:     # on joue milieu si libre
			t[1,1] = 2
		else:					# sinon place par défaut
			t[y_defaut,x_defaut] = 2
			

				
		
		
	

t=zeros([3,3],int)   # t[y,x] y=3 et x=3                     
                                
t[0,] = [0,0,0]
t[1,] = [0,0,0]
t[2,] = [0,0,0]


affiche_tableau(3,3)   # x et y 
fin = 0
nb_coups = 0
gagne = 0

while gagne == 0 and nb_coups < 9:
	joueur1()
	if aligner(1) ==1:
		gagne = 1
		print "JOUEUR 1 Gagne !"
	nb_coups = nb_coups + 1
	affiche_tableau(3,3)
	
	if gagne == 0 and nb_coups < 9:
		print
		print "coup ordinateur :"
		ordinateur()
		if aligner(2) ==1:
			gagne = 1
			print "ORDINATEUR gagne !"
		nb_coups = nb_coups+1
		
	affiche_tableau(3,3)
	
	if gagne == 0 and nb_coups == 9:
		print "match nul !"





	





                              
