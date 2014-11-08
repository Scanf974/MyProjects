# -*- coding: utf-8 -*-
# Calcul factoriel version récursive
# B. HOAREAU Dec 2011


def factoriel(n):
	# print "j'entre n=",n
	
	if n == 0:
		res = 1			# condition d'arrêt
	else:
	#	print "nouvel appel recursif avec n-1"
		res = n*factoriel(n-1)  # appel récursif avec n-1
	#	print "retour de l'appel recursif"
		
#	print "je sors n=",n," et res =",res
	
	return res

	
a = factoriel(1000)	
print a









	





                              
