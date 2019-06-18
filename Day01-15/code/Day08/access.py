class Test:
    """测试类的属性的私有性"""

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    '''
        两个下划线定义的变量默认为私有的
    '''
    print(Test.__init__)
    print("Test dict()", Test.__dict__)
    print("Test doc()", Test.__doc__)
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
