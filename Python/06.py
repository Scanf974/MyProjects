# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk


class Atome:
	"""atomes simplifiés, choisis parmi les 10 premiers éléments du TP"""
	
	table =[None, ('hydrogene',0), ('helium',2), ('lithium',4),('beryllium',5), ('bore',6), ('carbone',6), ('azote',7),('oxygene',8), ('fluor',10), ('neon',10)]
	
	def __init__(self, nat):
		"le n° atomique détermine le n. de protons, d'électrons et de neutrons"
		self.np, self.ne = nat, nat 									# nat = numéro atomique
		self.nn = Atome.table[nat][1]	 								# nb. de neutrons trouvés dans table
		self.nm = Atome.table[self.np][0]
		
	def affiche(self):
		print
		print "Nom de l'element :", self.nm
		print "%s protons, %s electrons, %s neutrons" % \
			(self.np, self.ne, self.nn)
		print
	
			
class Ion(Atome):
	"""les ions sont des atomes qui ont gagné ou perdu des électrons"""
	
	def __init__(self, nat, charge):
		"le n° atomique et la charge électrique déterminent l'ion"
		Atome.__init__(self, nat)
		self.ne = self.ne - charge
		self.charge = charge
		
	def affiche(self):
		"cette méthode remplace celle héritée de la classe parente"
		Atome.affiche(self)			 									# ... tout en l'utilisant elle-même !
		print "Particule electrisee. Charge =", self.charge
		print
		
### Programme principal : ###
a1 = Atome(1)
a2 = Ion(3, 1)
a3 = Ion(8, -2)

a1.affiche()
a2.affiche()
a3.affiche()
