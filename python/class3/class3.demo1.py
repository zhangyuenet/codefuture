# CodeFuture
# Class3 Demo1 : loop

classmate = ['Eason', 'Audrey','Steven','Alice','Wilson']

# loop style 1 
for name in classmate:
	print(name)

# loop style 2
num = len(classmate)
n = 0
while(n < num):
	print(classmate[n])
	n = n + 1

# break
num = len(classmate)
n = 0
while(n < num):
	if(n > 2):
		break
	print(classmate[n])
	n = n + 1

# continue
for name in classmate:
	if name == 'Alice':
		continue
	print(name)


# continue
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)



