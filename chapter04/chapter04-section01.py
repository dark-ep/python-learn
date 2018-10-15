#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce
from functools import reduce


def add(x, y):
    return x * 10 + y


print(reduce(add, [1, 3, 5, 7, 9]))  # f(f(f(x1, x2), x3), x4)

# 混合lanbda
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('1'))


def normalize(name):
    return str(name).lower().capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)  # ['Adam', 'Lisa', 'Bart']


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': ''}


def str2int(strs):
    return reduce(lambda x, y: x * 10 + y, map(lambda s: DIGITS[s], strs))


def str2float(s):
    index = s.find('.')
    s = s.replace('.', DIGITS.get('.'))
    return str2int(s) / pow(10, index)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
