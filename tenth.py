'''
类型注解
ctrl + p 可以调出辅助功能协助代码推断
'''
import json
import random

# 变量注解

var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = 'xding'

# 数据容器也是可以注解的 切实详细注解

my_list: list[int] = [1, 2, 3]  # 可以看到list 后面加上中括号是详细注解的意思
my_tuple: tuple[str, int, bool] = ("xding", 2, True)  # 如此优雅
my_set: set = {1, 2, 3}
my_dict: dict[int, str] = {1: 'xding'}  # 注意字典的注解分成 key value




# 第二种方法  用type 关键字标记
import random

var_5 = random.randint(1, 10)  # type: int


# var_6 = json.loads(data)  # type: dict[str, int]


# 对函数进行注释

def calab(x: int, y: int):  # 对形参进行注释
    return x + y


print(calab(2, 4))


def func(data: list) -> list:  # 对函数的返回值进行注解
    return data


print(func([1, 2, 3]))


# 使用Union 而理性进行注解

from typing import Union

mylist: list[Union[int, str]] = [1, 2, 'xding']

def function1(data: Union[int, str]) -> Union[int, str]:
    pass

function1(P)   # 此时ctrl + p 又提示