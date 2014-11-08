# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk
import os
from turtle import *

class Point:
	"un teste de distance"

class Rectangle:
	"définition d'une classe de rectangles"	
	
	
def trouveCentre(box):
	p = Point()
	p.x1 = box.coin.x + box.largeur/2.0
	p.y = box.coin.y + box.hauteur/2.0
	return p

p1 = Point()
p1.x = 1
p1.y = 2
p2 = p1


boite = Rectangle()
boite.largeur = 50.0
boite.hauteur = 35.0

boite.coin = Point()
boite.coin.x = 12.0
boite.coin.y = 27.0

centre = trouveCentre(boite)
print centre.x1, centre.y
