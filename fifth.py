class Student:
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    # 利用___init__ 魔术方法  类对象转变成字符串的行为
    def __str__(self):
        return f"Student 类对象，name:{self.name}, AGE : {self.age}"

stu = Student('xding', 33)
print(stu)
print(stu.age)
print(str(stu))
