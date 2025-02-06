"""
Created on 2025-02-06
"""

# Your code starts here

import copy


def use_list_copy():
    a = [1, 2, 3]
    b = a.copy()
    a[0] = 0
    print(a)
    print(b)


def use_copy():
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 0
    print(c)
    print(d)


def use_copy2():
    """
    浅拷贝只拷贝了第一层，第二层还是引用
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    print(id(c[0]))
    print(id(d[0]))

def use_deepcopy():
    """
    深拷贝拷贝了所有层
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    print(id(c[0]))
    print(id(d[0]))


if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    #use_copy2()
    use_deepcopy()
