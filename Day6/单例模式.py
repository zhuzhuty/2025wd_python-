"""
Created on 2025-01-23
"""


# Your code starts here
class MusicPlayer():
    instance = None

    def __new__(cls, *args, **kwargs):  # 重写new方法
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    player1 = MusicPlayer('player1')
    player2 = MusicPlayer('player2')
    print(id(player1))
    print(id(player2))
    print(id(player1) == id(player2))