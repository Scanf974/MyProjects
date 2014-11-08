# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *

I1 = 1.5
I2 = 1.6

x = 50.0


fx = x*x*x + x 
fpx = 3*x*x + 1

for i in range(1,20):
	fx = x*x*x + x - 5
	fpx = 3*x*x + 1
	x = x - (fx/fpx)
	
	print "x",i, "=",x


