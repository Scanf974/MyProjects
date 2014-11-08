# -*- coding: utf-8 -*-
# Programme Tri Rapide 

import random

def remplir_liste(nb_elements):
	
	for i in range(nb_elements):
		nb = random.randint(0,20)
		t.append(nb)
	
def affiche_liste(nb_elements):
	for i in range(nb_elements):
		print t[i],

def affiche2(debut,fin):
	print
	print "travail sur la sous liste :"
	for i in range(debut,fin+1,1):
		print t[i],
	

def echanger(i,indice):	# échange deux valeurs dans la liste t
	a= t[i]
	t[i] = t[indice]
	t[indice] = a
	

def tri_rapide(gauche, droite):
	
	print
	print "avant tri partiel :"
	affiche2(gauche,droite)	
	i = gauche
	j = droite
	milieu = int((i+j)/2)
	pivot = t[milieu]
	print "pivot = ",pivot
	
	while i<=j:
		while t[i]<pivot:
			i = i+1
		while t[j]>pivot:
			j = j-1
		
		if i<=j:
			echanger(i,j)
			i = i+1
			j = j-1

	# ici on a i>j 
	print "apres tri partiel "
	affiche2(gauche,droite)	
	print
	print "------------"
					
	if gauche<j:
		tri_rapide(gauche,j)
	
	if droite>i:
		tri_rapide(i,droite)
		
	
# Programme principal :

t=[]
remplir_liste(20)
print " Methode tri Rapide "
print "Liste NON triee :"
affiche_liste(20)
tri_rapide(0,19)
print
print "liste triee :"
affiche_liste(20)


	





                              
