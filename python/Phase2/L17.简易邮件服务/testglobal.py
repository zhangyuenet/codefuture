a = 0
b = 0

def funca() :
	a = 1
	print('funca a=%d' % a)

def funcb() :
	global b
	b = 1
	print('funcb b=%d' % b)

funca()
funcb()

print('a=%d' % a)
print('b=%d' % b)
