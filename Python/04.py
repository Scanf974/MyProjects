# -*- coding: utf-8 -*-

from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk



class Time:
	"Le temps en heurs, minutes, et secondes"
	def __init__(self, hh=0, mm=0 , ss=0):
		self.heur = hh
		self.minute = mm
		self.seconde = ss
		
	heur = 33
	
	def affiche_heur(self):
		print str(self.heur) + "'" + str(self.minute) + "\"" + str(self.seconde)
		print Time.heur
	
	
instant = Time()
instant.heur = 4
instant.minute = 9
instant.seconde = 52
instant.affiche_heur()

tps = Time(20,32,21)
tps.affiche_heur()
