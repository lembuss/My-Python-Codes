# this program works like a 7 segment LED 

def zero():

	global a
	
	a = '''
	###
	# #
	# #
	# #
	###
		'''

	return(a)

def one():

	global a
	
	a = '''
	#
	#
	#
	#
	#
		'''

	return(a)

def two():

	global a
	
	a = '''
	###
	  #
	###
	#
	###
		'''

	return(a)


def three():

	global a
	
	a = '''
	###
	  #
	###
	  #
	###
		'''

	return(a)

def four():

	global a
	
	a = '''
	# #
	# #
	###
	  #	
	  #
		'''

	return(a)


def five():

	global a
	
	a = '''
	###
	#
	###
	  #
	###
		'''

	return(a)

def six():

	global a

	a = '''
	###
	#
	###
	# #
	###
		'''

	return(a)


def seven():

	global a

	a = '''
	###
	  #
	  #
	  #
	  #
		'''

	return(a)


def eight():

	global a

	a = '''
	###
	# #
	###
	# #
	###
		'''

	return(a)




def nine():

	global a

	a = '''
	###
	# #
	###
	  #
	###
		'''

	return(a)

def decider(num):
	if num == 0:
		zero()

	elif num == 1:
		one()

	elif num == 2:
		two()

	elif num == 3:
		three()

	elif num == 4:
		four()

	elif num == 5:
		five()

	elif num == 6:
		six()

	elif num == 7:
		seven()

	elif num == 8:
		eight()

	elif num == 9:
		nine()


while(True):

	num =  input("Enter a number for display on the LED: ")
	

	for i in num:
		digit = int(i)
		decider(digit)
		a = a + a

	print(a)

	

