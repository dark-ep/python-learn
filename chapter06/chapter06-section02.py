#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):  # __init__方法的第一个参数永远是self
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


def set_score(self, score):
    if 0 <= score <= 100:
        self.__score = score
    else:
        raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
# print(bart.__name)
print(bart.get_name())
print(bart._Student__name)  # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
