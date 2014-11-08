# -*- coding: utf-8 -*-

# en paramètre : la base dans laquelle on va convertir le nombre décimal
# Méthode de la division par la base

def convertir(base,nombre):
	global reste
	nb=nombre
	i=-1
	while nb > 0:
		i=i+1
		quotient = nb/base
		reste[i] = nb-(quotient*base)
		nb=quotient
			
	print	
	for j in range(i,-1,-1):
		print reste[j],
		
reste=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


convertir(2,37)       # 2 c'est la base, 37 le nb à convertir
			
	
                                
