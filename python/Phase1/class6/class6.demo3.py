f = open('test.txt', 'w')
n = 1
while n < 101 :
	f.write('line%s\n' % n)
	n = n + 1
f.close()