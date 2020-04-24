# coding: UTF-8
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [3, 4, 3, 8, 9, 19, 20, 29, 0, 1, 3, 7, 1, 8, 3, 2, 3, 1, 1, 1]

plt.figure(figsize=(20, 8), dpi=80)

_font = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/Songti.ttc')

_x = [f'{i}岁' for i in x[::3]]
plt.xticks(x[::3], _x, fontproperties=_font)
# plt.yticks(range(min(y), max(y) + 1))
plt.yticks(range(min(y_2), max(y_2) + 1))
plt.xlabel("年龄", fontproperties=_font)
plt.ylabel("男(女)朋友个数", fontproperties=_font, rotation=-90)

plt.plot(x, y, label="自己")
plt.plot(x, y_2, label="同桌")

# set legend
plt.legend(prop=_font, loc="best")

plt.show()
