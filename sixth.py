'''
演示面向对象封装思想中私有成员的使用

私有的东西不能被外部调用但是可以被内部成员使用
'''

# 定义一个类，内含私有成员变量和私有方法

class Phone:
    __current_voltage = 2
    def __keep_single_core(self):
        print("keep a single core working")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("can use 5G calling")
        else:
            self.__keep_single_core()
            print("voltage too low can only use single core for calling")

phone = Phone()
phone.call_by_5G()