str_weight = input("input weight(kg, for example: 85):")
str_high = input("input high(m, for example: 1.7):")
weight = float(str_weight)
high = float(str_high)
bmi = weight / (high * high)
print(bmi)
if bmi < 18.5:
	print('Ultralight')
elif bmi >= 18.5 and bmi < 25:
	print('normal')
elif bmi >= 25 and bmi < 28:
	print('overweight')
elif bmi >= 28 and bmi < 32:
	print('obesity')
else :
	print('Severe obesity')
