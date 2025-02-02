"""
Created on 2025-01-21
"""


# Your code starts here
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet = 0

    def add_bullet(self, count):
        self.bullet += count
        print(f'加入了{count}颗子弹，剩余{self.bullet}颗子弹')

    def shoot(self):
        if self.bullet <= 0:
            print('没有子弹了')
            return
        self.bullet -= 1
        print(f'{self.model}发射了一颗子弹，剩余子弹还有{self.bullet}颗')


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print(f'{self.name}没有枪，无法开火')
            return
        self.gun.shoot()


if __name__ == '__main__':
    Ak = Gun('ak47')
    Ak.add_bullet(20)
    mike = Soldier('mike', Ak)
    mike.fire()
