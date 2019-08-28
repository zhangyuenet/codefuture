x = []
n = 1
while n <= 100 :
	if n % 2 == 0 :
		x.append(str(n))
	else:
		x.append(n)
	n = n + 1
s = ''
for item in x:
	s = s + str(item)
print(s)