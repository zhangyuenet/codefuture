f = open('test.txt', 'wb')
s = '你好'.encode('utf-7')
f.write(s)
f.close()


f = open('test.txt', 'rb')
s = f.read()
print(s)
f.close()
print(s.decode('utf-7'))


