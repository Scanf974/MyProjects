# -*- coding: utf-8 -*-


from scipy import *
from Tkinter import *
from math import *
import time
import winsound
import threading
import ImageTk


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


def animg():
	global an,image_1,image_2,image_3,image_4,image_5,image_6,image_7,image_8,image_9,image_10,image_11,image_12,image_13,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13
	an = an + 1
	if an == 1:
		image_1 = ImageTk.PhotoImage(file='projet/img/animbird/1.png')
		f1 = can.create_image(0, 0, image=image_1, anchor=NW)
		can.delete(f13)
	if an == 2:
		image_2 = ImageTk.PhotoImage(file='projet/img/animbird/2.png')
		f2 = can.create_image(0, 0, image=image_2, anchor=NW)
		can.delete(f1)
	if an == 3:
		image_3 = ImageTk.PhotoImage(file='projet/img/animbird/3.png')
		f3 = can.create_image(0, 0, image=image_3, anchor=NW)
		can.delete(f2)
	if an == 4:
		image_4 = ImageTk.PhotoImage(file='projet/img/animbird/4.png')
		f4 = can.create_image(0, 0, image=image_4, anchor=NW)
		can.delete(f3)
		
	if an == 5:
		image_5 = ImageTk.PhotoImage(file='projet/img/animbird/5.png')
		f5 = can.create_image(0, 0, image=image_5, anchor=NW)
		can.delete(f4)
		
	if an == 6:
		image_6 = ImageTk.PhotoImage(file='projet/img/animbird/6.png')
		f6 = can.create_image(0, 0, image=image_6, anchor=NW)
		can.delete(f5)
		
	if an == 7:
		image_7 = ImageTk.PhotoImage(file='projet/img/animbird/7.png')
		f7 = can.create_image(0, 0, image=image_7, anchor=NW)
		can.delete(f6)
		
	if an == 8:
		image_8 = ImageTk.PhotoImage(file='projet/img/animbird/8.png')
		f8 = can.create_image(0, 0, image=image_8, anchor=NW)
		can.delete(f7)
		
	if an == 9:
		image_9 = ImageTk.PhotoImage(file='projet/img/animbird/9.png')
		f9 = can.create_image(0, 0, image=image_9, anchor=NW)
		can.delete(f8)
		
	if an == 10:
		image_10 = ImageTk.PhotoImage(file='projet/img/animbird/10.png')
		f10 = can.create_image(0, 0, image=image_10, anchor=NW)
		can.delete(f9)
		
	if an == 11:
		image_11 = ImageTk.PhotoImage(file='projet/img/animbird/11.png')
		f11 = can.create_image(0, 0, image=image_11, anchor=NW)
		can.delete(f10)
		
	if an == 12:
		image_12 = ImageTk.PhotoImage(file='projet/img/animbird/12.png')
		f12 = can.create_image(0, 0, image=image_12, anchor=NW)
		can.delete(f11)
		
	if an == 13:
		image_13 = ImageTk.PhotoImage(file='projet/img/animbird/13.png')
		f13 = can.create_image(0, 0, image=image_13, anchor=NW)
		can.delete(f12)
		
		
		an =0	


#fenetre
fen = Tk()
fen.title("Angry Chicken")												
frame = Frame(fen)
frame.pack()


# Créer une fenêtre graphique fond couleur
can = Canvas(fen, width =1198, height =498, bg ='blue')
can.pack(side =TOP, padx =50, pady =20)

an = 0
timer_animg = MyTimer(0.04,animg)
timer_animg.start()


# fen.destroy()
fen.mainloop()
