# -*- coding: utf-8 -*-

def facto(n):
	if n == 0:
		res = 1
	else:
		res = 2*facto(n-1)
		print res
	return res


while 1:
	a = input("a= ")	
	facto(a)

