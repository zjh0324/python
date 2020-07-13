

# class 声明类的名字
# 类的名字首字母必须大写
# 面向对象编程
# 类里面所有的方法都必须传一个参数，叫self


class Girlfriend():
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age

    def caiyi(self,num):
        if num == 1:
            print('胸口碎大石')
        if num == 2:
            print('唱跳RAP篮球')
        if num == 3:
            print('单手开瓶盖')

    def chuyi(self):
        print('精通八大菜系')

    def work(self):
        print('开挖掘机！')

# # 类的实例化
# zhagnsan = Girlfriend('女','163cm','60kg','黑长直','22岁')
# zhagnsan.caiyi(2)
# zhagnsan.work()

# print(zhagnsan.high)
# print(zhagnsan.sex)
# '''
# class Car():
#     def __init__(self,pinpai,yanse,neishi,jilun):
#         self.pinpai = pinpai
#         self.yanse = yanse
#         self.neishi = neishi
#         self.jilun = jilun
#     def bianxing(self):
#         print('车子变身位金刚葫芦娃')
#     def fly(self):
#         print('车子开始起飞')

# zhagnsan = Car('凯迪拉克','红色','豪华','独轮车')
# zhagnsan.bianxing()

class Nvpy(Girlfriend):
    def work(self):
        print('修电脑')

object
zhagnsan = Nvpy('女','165','120','短发','25')
zhagnsan.work()