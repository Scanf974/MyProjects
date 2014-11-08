# -*- coding: utf-8 -*-

import random
from scipy import *

def tab(y1,x1) :
	for y in range (y1) :
		for x in range (x1) :
			print t[y,x],
		print 

 

def deplace(pyt,pxt,pu,a,py):		#pu puissance de tire
	pu = 1/ pu					#a angle
	px1 = 0.00
	py3 = py						#->
	py2 = int(py3)						#---> arondir le nombre
	py1 = py3-py2						#->
	if py1 > 0.5:						#->
		py1=py2+1						#->
	else:								#->
		py1=py2							#->
	t[py1,px1] = 7						#->
	while t[py1,px1+1] == 0:

		px1 = px1 + 1
		py3 = pu*px1*px1 - a*px1  + py	#->
		py2 = int(py3)						#---> arondir le nombre
		py1 = py3-py2						#->
		if py1 > 0.5:						#->
			py1=py2+1						#->
		else:								#->
			py1=py2							#->
		print "x=",px1,
		print "y=",py3,
		print "arondi a",py1					#->
		t[py1,px1] = 7
		tab(pyt,pxt)
		



		
t=zeros([200,40],int)

px = 0.00
pyt = input("Entrer la hauteur du tableau: ")
t[pyt-1]=[1]
py = pyt-2
t[py,px]=7

tab(pyt,40)

a = input("regle l'angle du tire: ")
pu = input("regle la puissance du tire: ")
touche = raw_input("Tirez!!!!!!")
if touche=="":	
	deplace(pyt,40,pu,a,py)

