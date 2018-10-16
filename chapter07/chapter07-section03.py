#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal, RunnableMixIn):  # 狗狗
    pass


class Bat(Mammal, FlyableMixIn):  # 蝙蝠
    pass


class Parrot(Bird, FlyableMixIn):  # 鹦鹉
    pass


class Ostrich(Bird, RunnableMixIn):  # 鸵鸟
    pass
