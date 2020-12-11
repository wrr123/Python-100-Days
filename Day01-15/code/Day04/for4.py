"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
canDivision = []
# for x in range(2, end + 1):
for x in range(2, num - 1):
    if num % x == 0:
        canDivision.append(x)
        is_prime = False
        # break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
    print('%d能够被整数%s整除' % (num, canDivision))
