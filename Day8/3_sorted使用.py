"""
Created on 2025-02-05
"""

# Your code starts here
from operator import itemgetter, attrgetter

my_list = 'This is a test string from Andrew'.split()
print(my_list)


def firstletter_lower(s: str):
    return s.lower()


print(sorted(my_list))  # 默认按照ASCII码排序
print(sorted(my_list, key=firstletter_lower))  # 先执行FirstLetter_lower函数，再按照返回值排序
print(sorted(my_list, key=lambda x: x.lower()))  # 使用lambda函数，效果同上

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ]
print(sorted(student_tuples, key=lambda x: x[2]))  # 按照年龄排序
print(sorted(student_tuples, key=itemgetter(2)))  # 按照年龄排序，效果同上

# 多列排序
print(sorted(student_tuples, key=lambda x: (x[1], x[2])))  # 先按照成绩排序，再按照年龄排序
print(sorted(student_tuples, key=itemgetter(1, 2)))  # 先按照成绩排序，再按照年龄排序


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        """
        没有str方法，会调用repr方法.
        :return:
        """
        return repr({'姓名': self.name, '年龄': self.age, '成绩': self.grade})


stu1 = Student('john', 15, 'A')
print(stu1)

student_objects = [Student('john', 15, 'A'),
                   Student('jane', 12, 'B'),
                   Student('dave', 10, 'B')]

print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

