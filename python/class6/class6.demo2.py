orign_str = input('请输入任意字符串：')

# method 1 - index
# =========================================================
i = len(orign_str) - 1
result = ''
while i >= 0 :
	result = result + orign_str[i]
	i = i - 1

print('方法1 变更的字符串为：%s' % result)

# method 2 - list
# ==========================================================
alist = []
i = 0
while i < len(orign_str) :
	alist.insert(0, orign_str[i])
	i = i + 1


print('方法2 变更的字符串为： %s' % alist)




# method 3



