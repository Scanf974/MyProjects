# -*- coding: utf-8 -*-
# Calcul factoriel
# B. HOAREAU Dec 2011

def factoriel(n):
	a = 1
	for i in range(n,0,-1):   # i va de n à 1
		a = a*i
	
	return a

def factoriel2(n):
	if n == 0:
		res = 1			# condition d'arrêt
	else:
		res = n*factoriel(n-1)  # appel récursif avec n-1
		
	return res

	
a = factoriel2(4)	
print a









	





                              
