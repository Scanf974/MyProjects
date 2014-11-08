# -*- coding: utf-8 -*-
#0.2
import random
import decimal
from scipy import*

def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		




t = zeros([11,21],int)



px1 = 0.00
py1 = (px1-10)*(px1-10)/10	

t[py1,px1]=7
tab(11,21)

print px1,py1

while 1:
	a = raw_input("")
	if a == "0":
		if t[py1,px1+1]==0:	#a remplacer plus tad dans def
			t[py1,px1]=0
			px1 = px1 +1 
			py1 = (px1-10)*(px1-10)/10						
			t[py1,px1]=7
			tab(11,21)
			print px1,py1
			
