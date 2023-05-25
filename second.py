# 定义一个成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f'hello every one. I am {self.name},excuse me!')

    def say_hi2(self, mesg):  # 增加了一个外部传入的参数
        print(f'hello every one. I am {self.name},{mesg}')


stu1 = Student()
stu1.name = "xding"
stu1.say_hi2("oh oh oh ")

stu2 = Student()
stu2.name = "yuhe"
stu2.say_hi()

stu3 = Student()
stu3.name = 'yuhe'
stu3.say_hi2("I so excited to meet you , hope we have a good time !")