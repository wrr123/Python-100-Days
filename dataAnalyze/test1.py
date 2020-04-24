from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘制图片
plt.plot(x, y)
# 设置x轴刻度
_xticks_labels = [i/2 for i in range(4, 50)]
# plt.xticks(range(2, 26, 2))
plt.xticks(_xticks_labels[::2])
# 设置y轴刻度
plt.yticks(range(min(y), max(y) + 2))
# save picture
# plt.savefig('./test1.png')
# show picture
plt.show()
