'''
设计一个带有私有成员的手机
'''

class Phone:
    __is_5G_enable = False
    def __check_5G(self):
        if self.__is_5G_enable:
            print("5g is on")
        else:
            print("5G is off")

    def call_by_5G(self):
        self.__check_5G()
        print("calling on going")

phone = Phone()

phone.call_by_5G()