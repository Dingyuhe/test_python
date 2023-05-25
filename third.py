# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建2个闹钟的对象

clock1 = Clock()
clock1.id = 1000
clock1.price = 10.2
print(f"闹钟ID：{clock1.id},价格是{clock1.price}")
clock1.ring()


clock2 = Clock()
clock2.id = 1001
clock2.price = 10.5
print(f"闹钟ID：{clock1.id},价格是{clock1.price}")
clock2.ring()

