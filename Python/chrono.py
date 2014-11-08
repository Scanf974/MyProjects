# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
import time
import winsound
import threading
import ImageTk
import os



class MyTimer:
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
        
    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()
        




def chrono():
	global ss,mm,hh

	ss = ss + 1
	if ss == 60:
		ss = 0
		mm = mm + 1
	if mm == 60:
		mm = 0
		hh = hh + 1
	os.system("cls")
	print hh,"h ",mm,"min ",ss,"s"

	

							
		
		
	

timer_cr = MyTimer(1,chrono)

ss = 0
mm = 0
hh = 0

a = raw_input("Demarrer le chrono?")
timer_cr.start()


