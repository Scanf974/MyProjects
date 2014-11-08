# -*- coding: utf-8 -*-
# Programme Morpion
# Version humain contre humain

import random
from scipy import *

def affiche_tableau(x1,y1):
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
	ok = 0
	while ok==0:
		x,y = input("ORDINATEUR entrer x , y :")	
		if t[y,x] ==0:
			t[y,x] = 2
			ok = 1
		else:
			print "erreur, recommencer"
		
	

t=zeros([3,3],int)   # t[y,x] y=3 et x=3                     
                                
t[0,] = [0,0,0]
t[1,] = [0,0,0]
t[2,] = [0,0,0]



affiche_tableau(3,3)   # x et y 
print aligner(1)
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
		ordinateur()
		if aligner(2) ==1:
			gagne = 1
			print "ORDINATEUR gagne !"
		nb_coups = nb_coups + 1
		affiche_tableau(3,3)
	
	if gagne == 0 and nb_coups == 9:
		print "match nul !"





	





                              
