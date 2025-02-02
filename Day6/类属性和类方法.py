"""
Created on 2025-01-22
"""


# Your code starts here
class Tool:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    def __del__(self):
        Tool.count -= 1

    @classmethod  # 类方法
    def show_tool_count(cls):
        print(f'工具对象的数量是{cls.count}')

    @staticmethod  # 静态方法
    def help():
        print('这是一个工具类，用于创建工具对象')


if __name__ == '__main__':
    Tool.help()
    too1 = Tool('斧头')
    too2 = Tool('锤子')
    too3 = Tool('榔头')
    print(Tool.count)
    del too1
    print(Tool.count)
    Tool.show_tool_count()
