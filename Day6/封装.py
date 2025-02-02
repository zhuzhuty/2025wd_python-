"""
Created on 2025-01-21
"""


# Your code starts here

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name} is running,weight has decreased 0.5,weight now is {self.weight}')

    def eat(self):
        self.weight += 1
        print(f'{self.name} is eating,weight has increased 1,weight now is {self.weight}')

    def __str__(self):
        return f'my name is {self.name} and my weight is {self.weight}'


if __name__ == '__main__':
    elephant = Person('大象', 70)
    elephant.run()
    elephant.eat()
    print(elephant)
