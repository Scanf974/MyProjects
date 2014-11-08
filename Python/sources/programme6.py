# -*- coding: utf-8 -*-
# jeu du nombre aléatoire à rechercher 

import random

nb = random.randint(0,100)
trouve =0

while trouve == 0:
	N = input("Entrez un nombre entre 0 et 100 : ")
	if N<nb:
		print "Trop petit"
	if N>nb:
		print "Trop grand"
	if N==nb:
		print "Vous avez gagné !"
		trouve = 1



                              
