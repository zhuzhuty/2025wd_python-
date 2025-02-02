"""
Created on 2025-01-21
"""


# Your code starts here
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f'我的年龄是{self.__age}')

    def boyfriend(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('小红', 18)
    xiaohong.boyfriend()
