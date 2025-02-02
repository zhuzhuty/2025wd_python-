"""
Created on 2025-01-13
"""


# Your code starts here
def homework31():
    """
    以列表 [A,B’,C’D’,E’,F’，G’,H”]中的每一个元素为键，默认值都是0，创建一个字典。
    :return:
    """
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    dict1 = {(i, 0) for i in list1}
    print(f'homework31:{dict1}')


def homework32():
    """
    将二维结构[['a’,1],['b’,2]] 和(('x’,3),('y’,4))转成字典
    :return:
    """
    list1 = [['a', 1], ['b', 2]]
    tuple1 = (('x', 3), ('y', 4))
    dict1 = dict(list1 + list(tuple1))
    print(f'homework32:{dict1}')


def homework33():
    """
    将元组(1,2)和(3,4)合并成一个元组
    :return:
    """
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    tuple3 = tuple1 + tuple2
    print(f'homework33:{tuple3}')


def homework34():
    """
    将空间坐标元组(1,2,3)的三个元素解包对应到变量 x,y,z
    :return:
    """
    tuple1 = (1, 2, 3)
    x, y, z = tuple1
    print(f'homework34:{x},{y},{z}')


def homework35():
    """
    返回元组('Alice','Beth','Cecil’)中'Cecil'元素的索引号
    :return:
    """
    tuple1 = ('Alice', 'Beth', 'Cecil')
    print(tuple1.index('Cecil'))


def homework36():
    """
    返回元组(2,5,3,2,4)中元素 2 的个数。
    :return:
    """
    tuple1 = (2, 5, 3, 2, 4)
    print(tuple1.count(2))


def homework37():
    """
    判断'Cecil’ 是否在元组('Alice’,Beth’,'Cecil’)中。
    :return:
    """
    tuple1 = ('Alice', 'Beth', 'Cecil')
    print('Cecil' in tuple1)


def homework38():
    """
    返回在元组(2,5,3,7)索引号为2的位置插入元素9之后的新元组。
    :return:
    """
    tuple1 = (2, 5, 3, 7)
    tuple2 = tuple1[:2] + (9,) + tuple1[2:]
    print(tuple2)


def homework39():
    """
    创建一个空集合，增加{'x’,'y’,'z”}三个元素。
    :return:
    """
    set1 = set()
    set1.add('x')
    set1.add('y')
    set1.add('z')
    print(set1)


def homework40():
    """
    删除集合{'x’,'y’,'z’} 中的'z’元素，增加元素'w’，然后清空整个集合。
    :return:
    """
    set1 = {'x', 'y', 'z'}
    set1.remove('z')
    set1.add('w')
    set1.clear()
    print(set1)


def homework41():
    """
    返回集合{'A’,D’,B”} 中未出现在集合 {'D’,'E’,C”}中的元素(差集)
    :return:
    """
    set1 = {'A', 'D', 'B'}
    set2 = {'D', 'E', 'C'}
    print(set1 - set2)
    print(set1.difference(set2))


def homework42():
    """
    返回两个集合 {'A’,'D’,'B”} 和 {'D’,'E’，C”} 的井集。
    :return:
    """
    set1 = {'A', 'D', 'B'}
    set2 = {'D', 'E', 'C'}
    print(set1 & set2)


def homework43():
    """
    返回两个集合“'A’,D’,B” 和 {“D’,E’，C”}的交集。
    :return:
    """
    set1 = {'A', 'D', 'B'}
    set2 = {'D', 'E', 'C'}
    print(set1 | set2)


def homework44():
    """
    返回两个集合 “A’,'D’,B’ 和 {'D’,'E’，C”}未重复的元素的集合。(对称差集）
    :return:
    """
    set1 = {'A', 'D', 'B'}
    set2 = {'D', 'E', 'C'}
    print(set1 ^ set2)


def homework45():
    """
    判断两个集合{'A’,'D’,B”} 和 {D’,E’,C”是否有重复元素。
    :return:
    """
    set1 = {'A', 'D', 'B'}
    set2 = {'D', 'E', 'C'}
    print(set1.isdisjoint(set2))


def homework46():
    """
    判断集合 {'A’,'℃’} 是否是集合 {'D’,“C’,'E’','A”} 的子集。
    :return:
    """
    set1 = {'A', 'C'}
    set2 = {'D', 'C', 'E', 'A'}
    print(set1.issubset(set2))


def homework47():
    """
    去除数组 [1,2,5,2,3,4,5,'x’,4,'x”] 中的重复元素。
    :return:
    """
    list1 = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
    list1 = list(set(list1))
    print(list1)


def homework48():
    """
    返回字符串'abCdEfg’的全部大写、全部小写和大下写互换形式。
    :return:
    """
    str1 = 'abCdEfg'

    print(str1.upper())
    print(str1.lower())
    print(str1.swapcase())


def homework49():
    """
    判断字符串'abCdEfg’是否首字母大写，字母是否全部小写，字母是否全部大写。
    :return:
    """
    str1 = 'abCdEfg'
    print(str1.istitle())
    print(str1.islower())
    print(str1.isupper())


def homework50():
    """
    返回字符串'this is python’首字母大写以及字符串内每个单词首字母大写形式
    :return:
    """
    str1 = 'this is python'
    print(str1.capitalize())
    print(str1.title())


def homework51():
    """
    判断字符串'this is python’是否以'this’开头，又是否以'python’ 结尾。
    :return:
    """
    str1 = 'this is python'
    print(str1.startswith('this'))
    print(str1.endswith('python'))


def homework52():
    """
    返回字符串'this is python’ 中'is’ 的出现次数。
    :return:
    """
    str1 = 'this is python'
    print(str1.count('is'))


def homework53():
    """
    返回字符串'this is python’中'is’首次出现和最后一次出现的位置。
    :return:
    """
    str1 = 'this is python'
    print(str1.index('is'))
    print(str1.rindex('is'))


def homework54():
    """
    将字符串'this is python’切片成3个单词。
    :return:
    """
    str1 = 'this is python'
    print(str1.split(' '))


def homework55():
    """
    返回字符串'blog/csdn/net/xufive/article/details/102946961'按路径分隔符切片的结果
    :return:
    """
    str1 = 'blog.csdn.net/xufive/article/details/102946961'
    print(str1.splitlines())


if __name__ == '__main__':
    homework31()
    homework32()
    homework33()
    homework34()
    homework35()
    homework36()
    homework37()
    homework38()
    homework39()
    homework40()
    homework41()
    homework42()
    homework43()
    homework44()
    homework45()
    homework46()
    homework47()
    homework48()
    homework49()
    homework50()
    homework51()
    homework52()
    homework53()
    homework54()
    homework55()
