# -*- coding: utf-8 -*-
# Programme Tri par minimum

import random

def remplir_liste(nb_elements):
	
	for i in range(nb_elements):
		nb = random.randint(0,20)
		t.append(nb)
	
def affiche_liste(nb_elements):
	for i in range(nb_elements):
		print t[i],


def echanger(i,indice):	# échange deux valeurs dans la liste t
	a= t[i]
	t[i] = t[indice]
	t[indice] = a
	

def minimum(debut, nb_elements):
	indice = debut
	for i in range(debut+1,nb_elements,1):
		if t[i]<t[indice]:		# si je trouve un élément plus petit
			indice = i			# je conserve sa position dans indice

	return indice


def trier(nb_elements):
	for i in range(nb_elements-1):
		indice = minimum(i,nb_elements)
		if i<> indice:
			echanger(i,indice)
			print
			affiche_liste(20)
			

# Programme principal :

t=[]
remplir_liste(20)
print "Liste NON triee :"
affiche_liste(20)
trier(20)
print
print "liste triee :"
affiche_liste(20)


	





                              
