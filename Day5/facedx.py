"""
Created on 2025-01-20
"""


# Your code starts here
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running')

    def eat(self):
        print(f'{self.name} is eating')
    def introduce(self):
        print(f'我叫{self.name},今年{self.age}岁')

xm=Person('小明',18)

xm.introduce()
xm.eat()
xm.run()

class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print(f'{self.name}是{self.color}的,汪汪叫')

doge=Dog('旺财','黄色')
doge.bark()
