class Student:
    name = None   #类中的属性 姓名年龄 国籍等
    gender = None
    nationality = None
    native_place = None
    age = None


stu1 = Student()  #创建对象

stu1.name = 'xding'     #对象属性赋值
stu1.gender = 'male'
stu1.age = 33
stu1.nationality = 'China'
stu1.native_place = 'Anhui'

#获取对象中记录的信息
print(stu1.age)
print(stu1.name)
print(stu1.nationality)
print(stu1.native_place)
