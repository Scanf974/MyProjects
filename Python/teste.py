# -*- coding: utf-8 -*-

from scipy import *
from math import *
import os
import time

def tab(y1,x1) :
	for y in range (y1) :
		for x in range (x1) :
			print t[y,x],
		print 

def deplace(py1,px1,px0,py0):
	g = 9.81
	angd = 40															#0 a 90 DEGRES
	angr = 0.0174*angd													#0 a 1.5 RADIAN
	v0 = 10
	vx0 = cos(angr)*v0
	vy0 = sin(angr)*v0
	
	tps = 0
	px = 0
	py = 0
	while t[py,px+1] == 0:
		tps = tps + 0.1
		px = vx0*tps + px0
		py = g/2*tps*tps - vy0*tps + py0
		t[py,px]=1
		tab(py1,px1)
		print vx0
		print "temps = ",tps,"s"
		print "x =",px
		print "y= ",py
		print
		time.sleep(0.1)
		os.system("cls")

t=zeros([2000,400],int)
px0 = 10
py0 = 10
t[py0,px0]=7

g = 9.81
angle = 45
v0 = 1
vx0 = cos(angle)*v0
vy0 = -sin(angle)*v0
tps = 0

tab(20,40)
while 1:
	touche = raw_input("Tirez!!!!!!")
	if touche=="":	
		deplace(20,40,px0,py0)
		

							

