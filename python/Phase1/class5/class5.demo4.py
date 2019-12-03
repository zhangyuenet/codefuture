f = open('password.txt','r')
pwtable = {}
for line in f.readlines():
    items = line.strip().split(';') # 把末尾的'\n'删掉，并分成三部分
    if len(items) == 3 :
    	pwtable[items[0]] = '用户名：%s；密码：%s' % (items[1],items[2])

f.close()

site = input('输入一个网站：')
print(pwtable[site])


