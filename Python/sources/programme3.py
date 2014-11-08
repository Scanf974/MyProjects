# -*- coding: utf-8 -*-
# Initiation à la programmation
# addition de nombres pairs

somme =0

N = input("Entrez la valeur de N : ")

print "N mod 5 = ",N%5

                              
for i in range(N):
	if i%2 == 0:
		print i
		somme = somme + i

print "somme des nombres pairs=", somme
