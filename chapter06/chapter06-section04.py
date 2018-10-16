#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

print(type(123) == type(456))  # True
print(type(123) == int)  # True
print(type('abc') == type('123'))  # True
print(type('abc') == str)  # True
print(type('abc') == type(123))  # False

import types


def fn():
    pass


print(type(fn) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type((x for x in range(10))) == types.GeneratorType)  # True


# isinstance
class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))  # True
print(isinstance(h, Dog))  # True
print(isinstance(h, Animal))  # True
print(isinstance(d, Dog) and isinstance(d, Animal))  # True
print(isinstance(d, Husky))  # False

print(isinstance('a', str))  # True
print(isinstance(123, int))  # True
print(isinstance(b'a', bytes))  # True
print(isinstance([1, 2, 3], (list, tuple)))  # True
print(isinstance((1, 2, 3), (list, tuple)))  # True

# dir
print(dir('ABC'))
print(len('ABC') == 'ABC'.__len__())  # True


class MyDog(object):

    def __len__(self):
        return 100


print(len(MyDog()))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y)  # 获取属性'y'
# print(getattr(obj, 'z')) # 获取属性'z'
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
print(dir(obj))
print(hasattr(obj, 'power'))  # 有属性'power'吗？
print(getattr(obj, 'power'))  # 获取属性'power'
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)  # fn指向obj.power
print(fn())
