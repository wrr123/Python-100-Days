def fib(num, temp=None):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    :param num:
    :param temp:
    :return:
    """
    temp = temp if temp else {}
    if num in (2, 3):
        return 1
    elif num == 1:
        return 0
    # try:
    #     return temp[num]
    # except KeyError:
    #     temp[num] = fib(num - 1) + fib(num - 2)
    #     return temp[num]
    return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    print(fib(10))
