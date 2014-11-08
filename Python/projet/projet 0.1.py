# -*- coding: utf-8 -*-
# 0.1
import random
import decimal
from scipy import*

def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		
def deplace(py1,px1):
	py1 = 20
	px1 = 0
	t[py1,px1]=7
	while t[py1,px1+1]==0:
		t[py1,px1]=0
		px1 = px1 +1 
		t[py1,px1]=7
		tab(22,40)

t = zeros([22,40],int)

t[21,]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]

deplace(22,40)


