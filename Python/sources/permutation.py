# -*- coding: utf-8 -*-
# Programme permutation en itératif 

numero =0

for i in range(4):
	for j in range(4):
		if j<>i:
			for k in range(4):
				if k<>i and k<>j:
					for l in range(4):
						if l<>i and l<>j and l<>k:
							numero = numero +1
							print i,j,k,l,"  n= ",numero
	





                              
