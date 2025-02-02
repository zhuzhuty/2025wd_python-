"""
Created on 2025-01-05
"""


# Your code starts here


def use_for():
    s = range(0, -10, -1)  # 开区间
    for i in s:
        print(i, end=" ")
    print()
    print(i)


use_for()
print('-' * 100)


def use_for2():
    my_list = ['ab', 'cd', 3]
    for i in my_list:
        print(i)


use_for2()
