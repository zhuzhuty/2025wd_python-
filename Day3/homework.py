"""
Created on 2025-01-09
"""


# Your code starts here
def homework1():
    """
    有7个整数，其中有3个数出现了两次，1个数出现了一次，找出出现了一次的那个数
    :return:
    """
    my_list = [1, 1, 2, 2, 3, 6, 6]
    result = 0
    for i in my_list:
        result ^= i
    print(result)
def homework2():
    """
    写一个简单的for循环，从1打印到20，横着打为1排
    :return:
    """
    for i in range(1,21):
        print(i,end=' ')

def homework6():
    """
    有8个整数，其中有3个数出现了两次，2个数出现了一次，找出出现了一次的那2个数。
    :return:
    """

if __name__ == '__main__':
    homework1()
    homework2()
