"""
Created on 2025-02-07
"""

# Your code starts here
import re


def use_search():
    """
    re.search(pattern, string, flags=0)
    :return:
    """
    ret = re.search(r'\d+', '阅读次数为 9999')
    print(ret.group())


def use_findall():
    """
    re.findall(pattern, string, flags=0)
    :return:
    """
    ret = re.findall(r'\d+', 'python = 9999, c = 7890, c++ = 12345')
    print(ret)


def use_sub():
    """
    re.sub(pattern, repl, string, count=0, flags=0)
    :return:
    """
    ret = re.sub(r'\d+', '998', 'python = 9999')
    print(ret)
    text = 'apple apple apple'
    ret = re.sub('apple', 'orange', text, count=2)
    print(ret)

def use_sub2():
    long_text="""
    <div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP 协议，熟悉MVC、MVVM 等概念以及相关WEB 开发框架</p>
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使用MySQL/PostgreSQL 中的一种<
br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
    </div>
    """
    ret = re.sub(r'<[^>]+>|&nbsp;|\s|\n','',long_text)
    print(ret)


def use_split():
    """
    re.split(pattern, string, maxsplit=0, flags=0)
    :return:
    """
    ret = re.split(r':| ', 'info:xiaoZhang 33 shandong')
    print(ret)

if __name__ == '__main__':
    use_search()
    use_findall()
    use_sub()
    use_sub2()
    use_split()


