# -*- coding: utf-8 -*-
# Programme tableau

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
			nb = random.randint(0,9)
			t[y,x] = nb
		
def tester_ligne(numero_ligne, n, x1,y1):	
	nb=0 	# nb de fois qu'on va trouver n
	for x in range(x1):
		if t[numero_ligne,x]==n:
			nb=nb+1
	return nb

def tester_diagonale1(x,y,x1,y1):
	nb=0     # nb de fois qu'on va trouver n
	ix=x
	iy=y
	n = t[y,x]
	while ix<x1-1 and iy<y1-1:
		ix = ix+1	# Parcours diagonale bas droite
		iy = iy+1
		if t[iy,ix] == n:
			nb = nb+1
			
	ix=x
	iy=y
	
	while ix>0 and iy>0:
		ix = ix-1	# Parcours diagonale haut gauche
		iy = iy-1
		if t[iy,ix] == n:
			nb = nb+1
						
	return nb,n
			
def tester_diagonale2(x,y,x1,y1):
	nb=0     # nb de fois qu'on va trouver n
	ix=x
	iy=y
	n = t[y,x]
	while ix<x1-1 and iy>0:
		ix = ix+1	# Parcours diagonale haut droite
		iy = iy-1
		if t[iy,ix] == n:
			nb = nb+1
			
	ix=x
	iy=y
	
	while ix>0 and iy<y1-1:
		ix = ix-1	# Parcours diagonale bas gauche
		iy = iy+1
		if t[iy,ix] == n:
			nb = nb+1
						
	return nb,n

t=zeros([8,10],int)   # t[y,x] y=8 et x=10                     
                                
t[0,] = [0,0,0,0,0,0,0,0,0,0]
t[1,] = [0,0,0,0,0,0,0,0,0,0]
t[2,] = [0,0,0,0,0,0,0,0,0,0]
t[3,] = [0,0,0,0,0,0,0,0,0,0]
t[4,] = [0,0,0,0,0,0,0,0,0,0]
t[5,] = [0,0,0,0,0,0,0,0,0,0]
t[6,] = [0,0,0,0,0,0,0,0,0,0]
t[7,] = [0,0,0,0,0,0,0,0,0,0]


remplir_tableau(10,8)
affiche_tableau(10,8)

a= tester_ligne(2,4,10,8)
print "le nombre 4 apparait", a," fois dans la ligne 2"

a,n = tester_diagonale1(4,4,10,8)
print "le nombre ",n,"aux coordonnees 4,4 apparait ",a," fois dans la diagonale \\"
a,n = tester_diagonale2(4,4,10,8)
print "le nombre ",n,"aux coordonnees 4,4 apparait ",a," fois dans la diagonale /"


	





                              
