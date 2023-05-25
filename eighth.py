'''
继承/复写/调用父类成员
super（）关键字
'''

class Phone:   # 定义一个父类
    IMEI = None
    producer = "ITCAST"

    def call_by_5G(self):
        print("use 5G calling on going !")

class MyPhone(Phone):   # 定义一个子类
    producer = "ITHEIMA"  # 复写父类的属性

    def call_by_5G(self):   # 复写父类中的方法
        print("turn on single cpu core ensure save voltage !")
        print(f"father producer is : {super().producer}")   # 调用父类中的属性
        super().call_by_5G()   #调用父类中的方法
        print("turn off single core ensure phone performance !")

phone = MyPhone()
print(phone.producer)
print(phone.call_by_5G())