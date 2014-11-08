# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *

def tab(ye,xe):
	for y in range(ye):
		for x in range(xe):
			
			t[y,x] = random.randint(0,100)
		
			
	print t

	
		


ye = 1
xe = 10



t = zeros([ye,xe],int)	
tab(ye,xe)

for j in range(1,xe):
		print t[0,j]
		
	
for i in range(1,xe):
	
	if t[0,i] < t[0,i-1]:
		t[0,i] = t[0,i-1]
		t[0,i-1] = t[0,j-1]
		print t
	
	

			
