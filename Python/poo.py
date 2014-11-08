# -*- coding: utf-8 -*-

def function1():
    print 'You chose one.'
def  function2():
    print 'You chose two.'
def  function3():
    print 'You chose three.'
#
# switch est notre dictionnaire de functions
switch = {
    'one': function1,
    'two': function2,
    'three': function3,
    }
while 1:
	#
	# le choix peut être 'one', 'two', or 'three'
	choice = raw_input('Enter one, two, or three :')
	#
	# call one of the functions
	try:
		result = switch[choice]
	except KeyError:
		print 'I didn\'t understand your choice.'
	else:
		result()
