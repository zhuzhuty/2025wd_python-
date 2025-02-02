"""
Created on 2025-01-26
"""

# Your code starts here
import os


def use_rename():
    os.rename('file1.txt', 'File1.txt')


def use_remove():
    os.remove('File1.txt')


def use_dir():
    dir_list = os.listdir('.')
    print(dir_list)
    print(os.getcwd())
    # os.mkdir('test')
    os.rmdir('test')


def dfs_dir(cur_path):
    """
    深度优先遍历目录
    :param cur_path:
    :return:
    """
    dir_list = os.listdir(cur_path)
    for i in dir_list:
        print(i)
        if os.path.isdir(i):
            dfs_dir(i)



if __name__ == '__main__':
    # use_rename()
    use_dir()
