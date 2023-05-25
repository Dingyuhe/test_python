'''
python 中的构造方法使用： __init__ 来实现

可以实现：
    1，在创建类对象（类构造）的时候，会自动执行
    2，在创建类对象（类构造）的时候，将传入的赞数自动传递给__init__方法使用。
'''


class Student:
    name = None
    age = None
    tel = None  # 这三个值其实不需要 后面构造方法中会有定义

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f'Student 创建了一个类')


stu1 = Student('xding', '33', '18795897708')
print(stu1.age)
print(stu1.tel)
print(stu1.name)
print(stu1)   # 会输出对应的内存地址  对于我们来说没有太大作用  此时需要用到模式方法
print("--"*20)
# 再创建一个类实例
stu2 = Student('yeyu', '30', '15300000')
print(stu2.age)
print(stu2.tel)
print(stu2.name)