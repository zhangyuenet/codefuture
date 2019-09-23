def power(x, n):
	result = 1
	while n > 0:
		result = result * x
		n = n - 1

	return result

print(power(2,3))
print(power(3,2))
print(power(0,1))
print(power(5,0))
print(power(5,-4))
print(power(-5,4))
