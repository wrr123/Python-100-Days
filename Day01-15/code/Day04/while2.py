"""
用while循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum1 = 0
num = 2
while num <= 100:
    sum1 += num
    num += 2
print(sum1)
