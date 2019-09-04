f = open('multilines.txt','r')
alist = []
for line in f.readlines():
	# strip()可以吧一行文字中前后的空格和一些换行符号去掉。
    alist.append(line.strip()) 
f.close()

print(alist)
