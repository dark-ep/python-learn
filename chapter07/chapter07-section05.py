#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Wed'])
print(Weekday.Thu.value)
print(day1 == Weekday.Mon)  # True
print(day1 == Weekday.Tue)  # False
print(Weekday(1) == Weekday.Mon)  # True
for name, member in Weekday.__members__.items():
    print(name, '=>', member)


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if not isinstance(gender, Gender):
            raise TypeError('输入类型错误!')
        self.gender = gender


# bart = Student('Bart', 'A') # 抛出异常
# if bart.gender == 'A':
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
