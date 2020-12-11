"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum1 = 0
for x in range(1, 101):
    sum1 += x
print(sum1)
print(sum(range(1, 101)))
