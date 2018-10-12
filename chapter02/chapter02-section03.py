#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
print(calc())
nums = [1, 2, 3]
print(calc(*nums))  # print(calc(nums[0], nums[1], nums[2]))


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)  # person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 关键字参数省略
def person1(name, age, *, city='Beijing', job):  # 指定某个参数名称
    print(name, age, city, job)


# person1('Jack', 24) # 编译成功，但执行失败
person1('Jack', 24, job='Engineer')


# 可变参数
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


def product(*numbers):
    if len(numbers) == 0:
        raise TypeError("error args")
    s = 1
    for n in numbers:
        s = s * n
    return s


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
