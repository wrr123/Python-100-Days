"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

print()
count = 0
for x1 in range(1, 8):
    for x2 in range(1, 8):
        for x3 in range(1, 8):
            for x4 in range(1, 8):
                if x1 + x2 + x3 + x4 == 8:
                    count += 1
                    print('x1 = %d, x2 = %d, x3 = %d, x4 = %d' % (x1, x2, x3, x4))
print('方程`x1 + x2 + x3 + x4 = 8`的正整数解的个数为%d个' % count)
