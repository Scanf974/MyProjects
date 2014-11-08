
# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *



def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			
			t[y,x] = random.randint(0,2)
			if t[y,x] == 1 and t[y,x-1] == 1:
				print "a la case" ,x
			
	print t



t = zeros([1,15],int)
tab(1,15)
