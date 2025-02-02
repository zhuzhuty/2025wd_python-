# 按位与
print(5 & 3)

# 按位或
print(5 | 3)

# 按位取反
print(~5)

# 按位异或
print(5 ^ 3)

# 左移
print(5 << 1)

# 右移
print(5 >> 1)

# input()函数
a = int(input('请输入一个数字：'))
print(a)
print(type(a))  # input()函数输入的数据类型是字符串
# 把输入的字符串转换为整型


# 大小写转换
letter = input('请输入一个字母：')
if ord(letter) >= 97:
    letter = chr(ord(letter) - 32)
else:
    letter = chr(ord(letter) + 32)
print(letter)
