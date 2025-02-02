"""
Created on 2025-01-23
"""

# Your code starts here
def exception1():
    while True:
        try:
            num = int(input('请输入一个整数：'))
            result = 8 / num
            print(result)

        except ValueError:
            print('请输入正确的整数')
        # except ZeroDivisionError:
        #     print('除数不能为0')
        except Exception as result:
            print(f'未知错误{result}')
            print(result.__traceback__.tb_frame.f_globals['__file__'])
            print(result.__traceback__.tb_lineno)
        else:
            print('尝试成功')
            break
        finally:
            print('无论是否出现错误，都会执行的代码')

if __name__=='__main__':
    exception1()