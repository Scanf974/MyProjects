# -*- coding: utf-8 -*-
# Initiation à la programmation
# addition de nombres pairs

somme =0
i=0.0

N = input("Entrez la valeur de N : ")

                              
while i<N-1:
	i = i+1
	if ((i/2) - int(i/2)) == 0:
		print i
		somme = somme + i

print "somme des nombres pairs :", somme
