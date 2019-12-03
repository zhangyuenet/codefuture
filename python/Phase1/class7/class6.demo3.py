def calc(*numbers):

	result = numbers[0]
	for n in numbers:
		if n < result:
			result = n
	return result

print(min())
print(min(5,8))
print(min(1,'2'))
print(min(1,3,5))
