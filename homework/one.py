'''
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    for i in range(number):
        print('*', end='')
    print()
'''

def fun2():
    numbers = [19, 20, 9, 7, 30]
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    print(f'最大的数为{max_number}')


def fun3():
    numbers = [3, 4, 9, 10 ,28, 4, 4]
    numbers_copy = numbers.copy()
    for number in numbers_copy:
        if numbers.count(number) > 1:
            numbers.remove(number)
    print(numbers)


phone = input('Phone: ')
numbers_dic = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": "Zero"}
phone_trans = ''
for number in phone:
    value = numbers_dic.get(number)
    if value is not None:
        phone_trans += value + ' '
print(phone_trans)
