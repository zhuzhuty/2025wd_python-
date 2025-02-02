"""
Created on 2025-01-26
"""


# Your code starts here
def open_r():
    file = open('file1.txt', mode='r', encoding='utf-8')
    print(file.read())
    file.close()


def open_rp():
    file = open('file1.txt', mode='r+', encoding='utf-8')  # 没有文件会报错
    print(file.read())
    file.write('你好')
    file.close()


def open_w():
    file = open('file1.txt', mode='w', encoding='utf-8')  # 没有文件会创建, 有文件会清空
    file.write('你好')
    file.close()


def open_a():
    file = open('file1.txt', mode='a', encoding='utf8')
    file.write('hello')
    file.close()


def open_readlines():
    file = open('file1.txt', mode='r', encoding='utf-8')
    # while True:
    #     text = file.readline()
    #     if not text:
    #         break
    #     print(text)
    text = file.readlines()
    for i in text:
        print(i, end='')
    file.close()


if __name__ == '__main__':
    # open_w()
    # open_rp()
    # open_a()
    open_readlines()
