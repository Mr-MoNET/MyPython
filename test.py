class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具 [%s] 占地面积 [%.2f]" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_type = []

    def __str__(self):
        return "户型 [%s] 占地面积 [%.2f] 剩余面积 [%.2f] 家具类型 %s" \
               % (self.house_type, self.area, self.free_area, self.item_type)

    # item默认是一个HouseItem的类对象
    def add_item(self, item):
        print("添加一个%s" % item)
        if item.area > self.area:
            print("太大了，无法添加")
        self.item_type.append(item.name)
        self.free_area -= item.area


class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def __str__(self):
        return "枪支 [%s]" % self.model

    def reload_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count < 0:
            print("%s no count!" % self.model)

        else:
            self.bullet_count -= 1
            print("%s is firing..." % self.model)
            print("Always have %d count" % self.bullet_count)


class Soldier:

    def __init__(self, name, gun):
        self.name = name
        # gun是一个Gun的类对象
        # 用于让士兵操作枪支
        self.gun = gun

    def __str__(self):
        return "士兵 [%s] 持有单兵装备 [%s]" % (self.name, self.gun)

    def fire(self):
        if self.gun is None:
            print("You are not a gun!")

        else:
            self.gun.reload_bullet(38)
            self.gun.shoot()


if __name__ == '__main__':
    smg = Gun("SMG")
    npc = Soldier("jaeger", smg)
    print(npc)
    npc.fire()
