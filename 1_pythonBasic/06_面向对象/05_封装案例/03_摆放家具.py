"""
需求:
1. 房⼦(House) 有 户型、总⾯积 和 家具名称列表
 – 新房⼦没有任何的家具

2. 家具(HouseItem) 有 名字 和 占地⾯积，
其中– 席梦思(bed) 占地 4 平⽶– ⾐柜(chest) 占地 2 平⽶– 餐桌(table) 占地 1.5 平⽶

3. 将以上三件家具添加到房⼦中

4. 打印房⼦时，要求输出:户型、总⾯积、剩余⾯积、家具名称列表
"""
class HouseItem:
    def __init__(self, name, area):
        self.name = name      # 家具名称
        self.area = area      # 占地面积
    def __str__(self):
        return f'{self.name}占地{self.area}'

class House:
    def __init__(self, h_type, area):
        self.h_type = h_type    # 户型
        self.total_area = area  # 总面积
        self.free_area = area   # 剩余面积
        self.item_list = []     # 家具列表
    def __str__(self):
        return f'{self.h_type}户型，总面积{self.total_area}，剩余面积{self.free_area}，家具有{self.item_list}'

    def add_item(self, item):
        if self.free_area > item.area:
            print(f'添加家具{item.name}成功')
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print('空间不足')


if __name__ == '__main__':
    # 创建家具对象
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    print(bed)
    print(chest)
    print(table)
    # 创建房子
    house = House('三室一厅', 100)
    print(house)
    house.add_item(bed)
    print(house)
    house.add_item(chest)
    print(house)
    house.add_item(table)
    print(house)

