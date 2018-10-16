#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))  # True
print(isinstance(b, Animal))  # True
print(isinstance(c, Dog))  # True
print(isinstance(c, Animal))  # True
print(isinstance(b, Dog))  # False


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
