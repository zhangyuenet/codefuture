str_age = input('age:')
age = int(str_age)
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('your age is', age)
	print('kid')
