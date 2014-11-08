
# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *

def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			
			t[y,x] = random.randint(1,10)
			if t[y,x] == 5:
				t[y+1,x] = 0
			print t[y,x],
		print 


y1 = 20
x1 = 20
t = zeros([y1+1,x1+1],int)
tab(y1,x1)
