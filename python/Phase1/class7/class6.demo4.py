def myAdd(*numbers) :
	result = 0
	for n in numbers:
		result = result + n
	return result

print('myAdd(1,2,3,4) = % s' % myAdd(1,2,3,4) )
print('myAdd(1) = % s' % myAdd(1) )
print('myAdd(1,2) = % s' % myAdd(1,2) )