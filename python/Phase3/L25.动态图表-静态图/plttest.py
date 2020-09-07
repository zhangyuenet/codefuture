import matplotlib.pyplot as plt


#plt.plot([1,2,3,4])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('x numbers')
plt.ylabel('y numbers')
plt.show()


#fig, ax = plt.subplots(figsize=(15,8))
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot()
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
ax.barh(['A','B','C','D'], [1,2,2,3])
plt.show()