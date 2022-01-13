class People(object):

    def __init__(self, name):
        self.name = name

    def play_with_animal(self, animal):
        print("%s is playing with the %s" % (self.name, animal.name))


class Animal(object):

    def __init__(self, name):
        self.name = name

    def shout(self):
        print("%s is shouting:" % self.name)

    # 定义静态方法
    @staticmethod
    def run():
        print("running...")


# 继承Animal类
class Dog(Animal):

    # 用子类的形参初始化父类的形参
    # super().__init__(name)
    def __init__(self, name):
        super().__init__(name)

    def shout(self):
        super().shout()
        print("汪汪汪")


# 继承Animal类
class Sheep(Animal):

    def __init__(self, name):
        super().__init__(name)

    def shout(self):
        super().shout()
        print("咩咩咩")


class SheepHappy(Sheep):

    # 派生喜羊羊类
    # 在调用super().__init__()时程序会嵌套调用喜羊羊类的两个基类
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def shout(self):
        # 同理，不单会调用喜羊羊类的直接基类，也会调用它的最初始的基类
        super().shout()
        print("我是喜羊羊")


if __name__ == "__main__":
    xiaoming = People("小明")
    dog = Dog("dog")
    sheep = Sheep("sheep")
    sheephappy = SheepHappy("sheephappy", "青青草原")
    dog.shout()
    print("This an ordinary sheep")
    sheep.shout()
    print("-----------------------")
    print("This a special sheep")
    sheephappy.shout()
    sheephappy.run()
