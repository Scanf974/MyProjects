# -*- coding: utf-8 -*-
# Initiation à la programmation
# addition de nombres pairs et impairs

somme_pair =0
somme_impair = 0
i=0.0

N = input("Entrez la valeur de N : ")

                              
while i<N-1:
	i = i+1
	if ((i/2) - int(i/2)) == 0:
		print i," est pair"
		somme_pair = somme_pair + i
	else:
		print i," est impair"
		somme_impair=somme_impair + i

print "somme des nombres pairs :", somme_pair
print "somme des nombres impairs :", somme_impair
