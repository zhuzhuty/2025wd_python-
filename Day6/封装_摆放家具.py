"""
Created on 2025-01-21
"""


# Your code starts here
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '%s的占地面积为%.2f' % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return '房子的户型为：%s , 总面积为 %.2f , 剩余面积为 %.2f\n 家具 %s' % (
            self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item: HouseItem):
        print(f'添加{item.name}到房子中')
        if self.free_area < item.area:
            print(f'{item.name}的面积太大，不能添加到房子中')
            return
        self.free_area -= item.area
        self.item_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem('床', 4)
    television = HouseItem('电视', 2)
    table = HouseItem('桌子', 4)

    print(bed)
    print(television)
    print(table)

    my_room = House('一间卧室', 8)
    my_room.add_item(bed)
    my_room.add_item(television)
    my_room.add_item(table)
