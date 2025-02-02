"""
Created on 2025-01-20
"""


# Your code starts here

# 缺省参数
def print_info(name, age, gender='男'):
    print(f'姓名：{name}, 年龄：{age},性别：{gender}')


# 变长参数
"""
*args: 会把多余的位置参数，转换成元组
**kwargs: 会把多余的关键字参数，转换成字典
"""


def demo(num, *args, **kwargs):
    print(num)

    demo2(*args, **kwargs)  # 拆包后传递给demo2


def demo2(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    print_info('小明', 18)
    print_info('小红', 20, '女')

    demo(1, 2, 3, 4, 5, a=1, b=2)
