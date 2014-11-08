# -*- coding: utf-8 -*-
#0.2
import random
import decimal
from scipy import*
from Tkinter import *
import time
import winsound
import Tkinter
import threading

def tab(y1,x1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		

def deplace(py,px,a,pu):		#a = angle de lancement
	pu = 1/pu					#pu = puissance de lancement
	px1 = 0.00					
	py1 = pu*px1*px1 - a*px1 + py-1
	t[py1,px1]=1
	while t[py1,px1+1]==0:	

		px1 = px1 +1 
		py1 = pu*px1*px1 - a*px1 + py-1					
		t[py1,px1]=1
		tab(py,px)
		print px1,py1	



t = zeros([26,40],int)
deplace(26,40,0.5,50.0)


	
