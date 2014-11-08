# -*- coding: utf-8 -*-

# Programme Les 8 Reines
# Début : 14/10/11    FIN : 14/10/11
# B. HOAREAU   
# Rechercher les positions pour placer 8 reines
# sur un échiquier 8*8 , sans que les reines ne puissent se tuer
# 92 solutions trouvées :-)

from scipy import *





def position(x,y):
	ok=1
	fin = 0
	x1=x
	y1=y
	while fin==0:			# Parcours ligne
		x1=x1-1

		if x1<0:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0

	fin = 0
	x1=x
	y1=y
	while fin==0:			# Parcours ligne
		x1=x1+1

		if x1>7:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0		
			

			
	fin = 0
	x1=x
	y1=y
	while fin==0:			# Parcours diagonale 1
		x1=x1-1
		y1=y1-1
		if x1<0 or y1<0:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0
			
	fin = 0
	x1=x
	y1=y
	while fin==0:			# Parcours diagonale 2
		x1=x1+1
		y1=y1+1
		if x1>7 or y1>7:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0
					
	fin = 0
	x1=x
	y1=y
	while fin==0:			# Parcours diagonale 3
		x1=x1+1
		y1=y1-1
		if x1>7 or y1<0:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0
			
	
	fin = 0			
	x1=x
	y1=y
	while fin==0:			# Parcours diagonale 4
		x1=x1-1
		y1=y1+1
		if x1<0 or y1>7:
			fin=1
		else:
			if t[y1,x1]>0:
				ok=0
			
				

		
		
	return ok				# renvoie 1 si on peux placer reine
			
def placer_reine(x,y,numero_reine):
	t[y,x] = numero_reine


def effacer_reine(x,y):
	t[y,x]=0


def place(x,numero_reine):
	global nb_position
	
	if numero_reine<9:
		for y in range(8):
			if position(x,y)==1:     # Si je peux placer reine
				placer_reine(x,y,numero_reine)
				place(x+1,numero_reine+1)	# placer colonne suivante
				effacer_reine(x,y) # j'efface pour nouvelle position
	else:
		nb_position = nb_position+1
		print "position :",nb_position		
		affiche_tableau()
		a = raw_input("appuyer sur entree")
			
	
def affiche_tableau():
	print "---------------------"
	for ky in range(8):
		for kx in range(8):
			print t[ky,kx],
		print
			
	print
	print
		
	print "---------------------"

	
def cherche():
	global nb_position

	place(0,1)





t=zeros([8,8],int)   # t[y,x] :  X=12 et Y=10 (inversé)
t2 = zeros([10*10,2],int)   # t2[index,2) va me servir pour sauvegarder les passages
                             
                                
t[0,] = [0,0,0,0,0,0,0,0]
t[1,] = [0,0,0,0,0,0,0,0]
t[2,] = [0,0,0,0,0,0,0,0]
t[3,] = [0,0,0,0,0,0,0,0]
t[4,] = [0,0,0,0,0,0,0,0]
t[5,] = [0,0,0,0,0,0,0,0]
t[6,] = [0,0,0,0,0,0,0,0]
t[7,] = [0,0,0,0,0,0,0,0]

# Variables globales
nb_position = 0	# nb de positions totales trouvées

cherche()

                                
                                
