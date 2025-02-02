# 自己定义变量赋值不同的数据类型并打印，并使用type()函数查看数据类型
def print_type():
    a = 1
    b = 1.1
    c = 'hello'
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {'name': 'Tom', 'age': 18}
    h = {1, 2, 3}
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
    print(type(h))





# 将整型转化为不同进制
def print_bin():
    a = 123
    print(bin(a))
    print(oct(a))
    print(hex(a))





# 实现从1到100之间的奇数求和
def sum_odd():
    i = 1
    result = 0
    while i <= 100:
        if i % 2 == 0:
            i += 1
            continue
        else:
            result += i
            i += 1
    print(f'result={result}')





def sum_odd2():
    print(sum([x for x in range(101) if x % 2 == 1]))





# 打印九九乘法表
def Multable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j}*{i}={i * j:-2d}', end=' ')
        print()





# 统计一个整数数二进制中1的个数（负数按照64位算，使用位运算）
def count1():
    a = int(input('请输入一个整数：'))
    a = a & 0xffffffffffffffff  # 按位与
    print(bin(a).count('1'))




if __name__ == '__main__':
    print_type()
    print_bin()
    sum_odd()
    sum_odd2()
    Multable()
    count1()