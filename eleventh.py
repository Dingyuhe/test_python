'''
多态：表示多种状态，即完成某个行为时，使用不通的对象得到不同的状态

'''


class Animal:  # 设计一个顶层设计  一个标准 没有具体实现过程
    def speak(self):
        pass


class Dog(Animal):  # 具体实现的一个类 继承了父类
    def speak(self):
        print("汪汪汪。。。。")


class Cat(Animal):  # 具体实现的一个类 继承了父类
    def speak(self):
        print("喵喵喵。。。。")


def make_noise(animal: Animal):  # 有点绕  看起来意思是make_noise 这个参数可以是一个类 且是父类，但是后续在调用的时候给定的是字类的对象。就是多态的思想
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
