
# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *



def tab(ye,xe):
	for y in range(ye):
		for x in range(xe):
			
			print t[y,x],
			
		print 


x0 = 0
p = 0
ye = 8
xe = 8

x1 = random.randint(0.0,xe)
y1 = random.randint(0.0,ye)
x2 = random.randint(0.0,xe)
y2 = random.randint(0.0,ye)

t = zeros([ye,xe],int)

t[y1,x1] = 2
t[y2,x2] = 1

tab(ye,xe)

print "reine 1: (",x1,":",y1,")"
print "reine 2: (",x2,":",y1,")"

x = x2-x1
y = y2-y1


print x,y

if x > 0:
	if x == -y:
		print "touche a en HAUT a DROITE"
		

	if x == y:
		print "touche a en BAS a DROITE"

if x < 0:
	if x == -y:
		print "touche a en BAS a GAUCHE"
		

	if x == y:
		print "touche a en HAUT a GAUCHE"





for i in range(x1+1,8,1):

	if t[y1,i] == 1:
		print "touche a DROITE"
		print
	
for i in range(x1-1,-1,-1):

	if t[y1,i] == 1:
		print "touche a GAUCHE!!"
		print
			
			
for i in range(y1+1,8,1):

	if t[i,x1] == 1:
		print "touche en BAS!!"
		print
	
for i in range(y1-1,-1,-1):

	if t[i,x1] == 1:
		print "touche en HAUT!!"
		print
			
			

