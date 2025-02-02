"""
Created on 2025-01-10
"""


# Your code starts here
def homework2():
    """
    求两个有序数字列表的公共元素
    :return:
    """
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 3, 4, 7, 8, 9]
    common_list = [x for x in list1 if x in list2]
    return common_list


def homework3():
    """
    给定一个n个整型元素的列表a，其中有一个元素出现次数超过n/2，求这个元素
    :return:
    """
    list1 = [2, 1, 3, 2, 4, 2, 2]
    n = len(list1)
    for i in list1:
        if list1.count(i) > n / 2:
            return i


def homework5():
    """
    将元组(1,2,3)和集合 {4,5,6}合并成一个列表
    :return:
    """
    tup1e = (1, 2, 3)
    s3t = {4, 5, 6}
    list1 = list(tup1e) + list(s3t)
    print(f'homework5:{list1}')


def homework6():
    """
    在列表[1,2,3,4,5,6]首尾分别添加整型元素 7 和 0
    :return:
    """
    list1 = [1, 2, 3, 4, 5, 6]
    list1.insert(0, 7)
    list1.append(0)
    print(f'homework6:{list1}')


def homework7():
    """
    反转列表[0,1,2,3,4,5,6,7]
    :return:
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7]
    list1.reverse()
    print(f'homework7:{list1}')


def homework8():
    """
    反转列表 [0,1,2,3,4,5,6,7] 后给出中元素5 的索引号
    :return:
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7]
    list1.reverse()
    print(f'homework8:{list1.index(5)}')


def homework9():
    """
    分别统计列表[True,False,0,1,2]中 True,False,0,1,2的元素个数，发现了什么?
    :return:
    """
    list1 = [True, False, 0, 1, 2]
    print('-' * 100)
    print(f'True:{list1.count(True)}')
    print(f'False:{list1.count(False)}')
    print(f'0:{list1.count(0)}')
    print(f'1:{list1.count(1)}')
    print(f'2:{list1.count(2)}')


def homework10():
    """
    从列表 [True,1,0,'x’,None,'x’,False,2,True]中删除元素'x’。
    :return:
    """
    list1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
    for i in list1:
        if i == 'x':
            list1.remove(i)
    print(f'homework10:{list1}')


def homework11():
    """
    从列表 [True,1,0,'x’,None,'x’,False,2,True]中删除索引号为4的元素。
    :return:
    """
    list1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
    list1.pop(4)
    print(f'homework11:{list1}')


def homework12():
    """
    删除列表中索引号为奇数的元素。
    :return:
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list1 = [list1[i] for i in range(len(list1)) if i % 2 == 0]  # 这里创建了一个新的列表
    print(f'homework12:{list1}')


def homework13():
    """
    清空列表中的所有元素。
    :return:
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list1.clear()
    print(f'homework13:{list1}')


def homework14():
    """
    对列表【3,0,8,5,7]分别做升序和降序排列
    :return:
    """
    list1 = [3, 0, 8, 5, 7]
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    print(f'homework14:{list2},{list3}')


def homework15():
    """
    将列表[3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
    :return:
    """
    list1 = [3, 0, 8, 5, 7]
    list1 = [1 if i > 5 else 0 for i in list1]
    print(f'homework15:{list1}')


def homework16():
    """
    遍历列表['x','y'，'z']，打印每一个元素及其对应的索引号
    :return:
    """
    list1 = ['x', 'y', 'z']
    print('homework16:', end=' ')
    for x in list1:
        print(f'{x}:{list1.index(x)}', end=' ')
    print()


def homework17():
    """
    将列表[0,1,2,3,4,5,6,7,8,9]拆分为奇数组和偶数组两个列表
    :return:
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_list = [x for x in list1 if x % 2 != 0]
    even_list = [x for x in list1 if x % 2 == 0]
    print(f'homework17:{odd_list},{even_list}')


def homework18():
    """
    分别根据每一行的首元素和尾元素大小对二维列表[[6,5],[3,7],[2,8]] 排序。
    相当于按6,3,2进行排序，除非第一个元素相等按第二个元素排序
    :return:
    """
    list1 = [[6, 5], [3, 7], [2, 8]]
    list1.sort(key=lambda x: (x[0], x[1]))
    print(f'homework18:{list1}')


def homework19():
    """
    从列表[1,4,7,2,5,8]索引为3的位置开始，依次插入列表['x','y','z']的所有元素。
    :return:
    """
    list1 = [1, 4, 7, 2, 5, 8]
    list2 = ['x', 'y', 'z']
    for i in range(len(list2)):
        list1.insert(3 + i, list2[i])
    print(f'homework19:{list1}')


def homework20():
    """
    快速生成由[5,50) 区间内的整数组成的列表
    :return:
    """
    list1 = [x for x in range(5, 50)]
    print(f'homework20:{list1}')


def homework22():
    """
    将列表['x’,'y’,'z”] 和 [1,2,3] 转成〖('x’,1),('y’,2),('z’,3)]的形式。
    :return:
    """
    list1 = ['x', 'y', 'z']
    list2 = [1, 2, 3]
    list3 = [(list1[i], list2[i]) for i in range(len(list1))]
    print(f'homework21:{list3}')


def homework23():
    """
    以列表形式返回字典{'Alice’:20,'Beth’:18,'Cecil’:21} 中所有的键
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    list1 = list(dict1.keys())
    print(f'homework22:{list1}')


def homework24():
    """
    以列表形式返回字典{'Alice’:20,'Beth’:18,'Cecil’:21} 中所有的值
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    list1 = list(dict1.values())
    print(f'homework23:{list1}')


def homework25():
    """
    以列表形式返回字典“Alice’:20,'Beth’:18,'Cecil:21}中所有键值对组成的元组。
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    list1 = list(dict1.items())
    print(f'homework24:{list1}')


def homework26():
    """
    向字典{Alice’: 20,'Beth’: 18,Cecil’:21}中追加'David’:19 键值对，更新Cecil的值为17。
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    dict1['David'] = 19
    dict1['Cecil'] = 17
    print(f'homework25:{dict1}')


def homework27():
    """
    删除字典f'Alice’: 20,'Beth’:18,'Cecil’:21}中的Beth键后，清空该字典。
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    del dict1['Beth']
    dict1.clear()
    print(f'homework26:{dict1}')


def homework28():
    """
    判断 David 和 Alice 是否在字典 {'Alice’:20,'Beth’: 18,'Cecil’:21}中。
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    a = 'David' in dict1.keys()
    b = 'Alice' in dict1.keys()
    print(f'homework27:{a},{b}')


def homework29():
    """
    谝历字曲{Alice’:20.'Beth’:18.'Cecil:21}打印键值对
    :return:
    """
    dict1 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print(f'{dict1.items()}')

if __name__ == '__main__':
    homework5()
    homework6()
    homework7()
    homework8()
    homework9()
    homework10()
    homework11()
    homework12()
    homework13()
    homework14()
    homework15()
    homework16()
    homework17()
    homework18()
    homework19()
    homework20()
    homework22()
    homework23()
    homework24()
    homework25()
    homework26()
    homework27()
    homework28()
    homework29()
