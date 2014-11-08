# -*- coding: utf-8 -*-

import random
from scipy import*

def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		
		
def empiler(y,x):
	global index
	index = index + 1
	pile[index,0] = y
	pile[index,1] = x
	
def depiler():
	global index
	pile[index,0] = y
	pile[index,1] = x
	index = index - 1
	
def snak(y1,x1):
	a = 0
	if t[y,x] == 0:
		t[y,x] = 1
		empiler
	return a



t = zeros([10,10],int)
py = random.randint(0,9)
px = random.randint(0,9)
t[py,px]=1
tab(10,10)

index = 0
fin = 0

while fin == 0:
	touche = raw_input("8546")
	if touche == "5":
		trou = snak(10,10)
		if trou == 1:
			tab(10,10)

