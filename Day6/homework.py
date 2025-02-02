"""
Created on 2025-01-23
"""


# Your code starts here
def homework5():
    """
    通过try进行异常捕捉，确保输入的内容一定是个整数，然后判断该整形数是否是对称的
    :return:
    """
    while True:
        try:
            num = int(input('请输入一个整数：'))
        except ValueError:
            print('请输入正确的整数')
        else:
            if str(num) == str(num)[::-1]:
                print(f'{num}是对称数')
            else:
                print(f'{num}不是对称数')
            break
        finally:
            print('无论是否出现错误，都会执行的代码')


if __name__ == '__main__':
    homework5()
