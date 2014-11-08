# -*- coding: utf-8 -*-
# Parcours d'arbres
# B. HOAREAU janv 2012

from scipy import *

def creer_arbre(nb_noeuds):
	n=0
	for i in range(nb_noeuds):
		n = n+1
		arbre[i,0] = n
		n = n+1
		arbre[i,1] = n
		
	for i in range(nb_noeuds,n+1,1):   # pour les feuilles
		arbre[i,0] = -1				# fils gauche à -1
		arbre[i,1] = -1				# fils droit à -1

def affiche_arbre(nb_noeuds):
	for i in range(nb_noeuds):
		print "noeud ",i," fils G: ",arbre[i,0]," fils droit: ",arbre[i,1]

arbre=zeros([100,2],int)   # arbre[noeud,0] = fils gauche et arbre[noeud,1] =fils droit                  	
	
creer_arbre(7)				# 7 correspond au nombre de noeuds hors feuille
affiche_arbre(2*7+1)		# il y a donc 15 noeuds feuilles inclues









	





                              
