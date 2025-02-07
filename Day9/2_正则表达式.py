"""
Created on 2025-02-06
"""

# Your code starts here
import re

result = re.match('wangdao', 'wangdao.cn')
print(result.group())

# 匹配单个字符
"""
字符 功能
.   匹配任意1 个字符（除了\n）
[ ] 匹配[ ]中列举的字符
\d  匹配数字，即0-9 decimal
\D  匹配非数字，即不是数字
\s  匹配空白，即空格，tab 键space
\S  匹配非空白
\w  匹配单词字符，即a-z、A-Z、0-9、_ (汉字) word
\W  匹配非单词字符
"""
ret = re.match(".", "M")
print(ret.group())
ret = re.match("t.o", "too")
print(ret.group())
ret = re.match("t.o", "two")
print(ret.group())

ret = re.match('[hH]ello', 'hello python')
print(ret.group())

ret = re.match('\dhello', '7hello python')
print(ret.group())

# 匹配多个字符
"""
字符  功能
*    匹配前一个字符出现0次或无限次
+    匹配前一个字符出现1次或无限次
?    匹配前一个字符出现1次或0次
{m}  匹配前一个字符出现m次
{m,} 匹配前一个字符至少出现m次
{m,n}匹配前一个字符出现m到n次
"""

ret = re.match('[A-Z][a-z]*', 'Abcdefg')
print(ret.group())

names = ['name1', '_name', '2_name', '__name__']
for name in names:
    ret = re.match('[a-zA-Z_]+[\w]*', name)
    if ret:
        print(f'{ret.group()} 是合法的变量名')
    else:
        print(f'{name} 不是合法的变量名')

ret = re.match('[0-9]?\d','09')
print(ret.group())

# 匹配开头和结尾
"""
字符  功能
^     匹配字符串开头
$     匹配字符串结尾
"""
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match('\w{4,20}@163\.com$', email)
    if ret:
        print(f'{ret.group()} 163邮箱')
    else:
        print(f'{email} 不是163邮箱')

# 匹配分组
"""
字符  功能
|     匹配左右任意一个表达式
(ab)  将括号中字符作为一个分组
\num    引用num分组匹配到的字符串
(?P<name>) 分组起别名
(?P=name)   引用别名为name分组匹配到的字符串
"""
ret = re.match('[1-9][0-9]|[0-9]$', '11')
print(ret.group())

ret = re.match('\w{4,20}@(163|126|qq)\.com$','test@126.com')
print(ret.group())

ret = re.match(r'<(?P<g1>\w+)>.*</(?P=g1)>','<html>hh</html>')
if ret:
    print(f'{ret.group()} 是HTML标签')
else:
    print('不是HTML标签')
