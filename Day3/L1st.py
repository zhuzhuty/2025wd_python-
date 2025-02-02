"""
Created on 2025-01-06
"""

# Your code starts here
name_list = ['zhangsan', 'lisi', 'wangwu']
print(name_list[0])
print(name_list.index('wangwu'))
name_list.append(10)
print(name_list)

temp_list = ['猪八戒', '孙悟空', '唐僧']
name_list.extend(temp_list)
print(name_list)

num_list = [4, 2, 6, 1, 9, 4]
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

print(num_list.count(4))