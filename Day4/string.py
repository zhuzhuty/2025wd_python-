"""
Created on 2025-01-08
"""


# Your code starts here
def str_find():
    s1 = 'abcdefgcdefg'
    print(s1.find('cd', 2, 5))  # 从2到5位置查找cd


def str_replace():
    s1 = 'abcdefgcdefg'
    print(s1.replace('cd', 'CD', 1))  # 替换一次


def str_split():
    s1 = 'abc def ghi'
    print(s1.split(' ', 1))  # 从左往右分割一次


def str_join():
    s1 = ['abc', 'def', 'ghi']
    print(' '.join(s1))  # 用空格连接


def str_slice():
    num_str = '0123456789'
    # 截取从2~5的字符串
    print(num_str[2:6])
    # 截取从2~末尾的字符串
    print(num_str[2:])
    # 截取从开始~5位置的字符串
    print(num_str[:6])
    # 从开始位置，每隔一个截取一个
    print(num_str[::2])
    # 截取从2到末尾-1的字符串
    print(num_str[2:-1])
    # 截取末尾2个字符
    print(num_str[-2:])
    # 字符串逆序
    print(num_str[::-1])


if __name__ == '__main__':
    str_find()
    str_replace()
    str_split()
    str_join()
    str_slice()