"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import time
import math

start = time.perf_counter()
for num in range(1, 10000):
    sum1 = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum1 += factor
            if 1 < factor != num / factor:
                sum1 += num / factor
    if sum1 == num:
        print(num)
end = time.perf_counter()
print("执行时间:", (end - start), "秒")

# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性
