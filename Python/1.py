# -*- coding: utf-8 -*-

u0 = input("Il faut payer cb le premier moi?: ")
n = input("Pendant conbien de mois?: ") 

u = 0
v = 1


print "Le premier moi = ",	
print u0
while v<n:
	v = v+1
	u = u+30
	print "Le moi" ,v,
	print "= ",
	print u+u0
