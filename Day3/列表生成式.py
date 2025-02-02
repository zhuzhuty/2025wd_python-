"""
Created on 2025-01-06
"""

# Your code starts here
# 列表生成式
my_list = [x for x in range(10)]
print(my_list)

# 两个for循环
my_list = [y for x in range(10) for y in range(x)]
print(my_list)

# 二维列表生成式
my_list = [[x for x in range(3)] for y in range(3)]
print(my_list)

# 二维转一维
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [x for y in a for x in y]
print(b)

# 过滤
my_list = [x for x in range(10) if x % 2 == 0]
print(my_list)
c=[x if x % 2 == 0 else x**2 for x in b]
print(c)