# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager as fm

"""
font = {'family': 'PingFang',
        'weight': 'bold',
        'size': '5.0'}
matplotlib.rc("font", **font)
"""
_font = fm.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

a = [random.randint(20, 35) for i in range(120)]
b = range(120)

plt.figure(figsize=(20, 8), dpi=80)
plt.yticks(range(min(a), max(a) + 2))

_b = [f'10点{i}分' for i in range(60)]
_b += [f'11点{i}分' for i in range(60)]
plt.xticks(b[::3], _b[::3], rotation=45, fontproperties=_font)

# 设置折线图的描述信息
plt.xlabel("时间", fontproperties=_font)
plt.ylabel("温度 (℃)", fontproperties=_font)
plt.title("10点到12点的时间温度变化情况", fontproperties=_font)

plt.plot(_b, a)
plt.show()
