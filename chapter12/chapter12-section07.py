#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# count,takewhile
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# cycle
cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
cL = []
for c in cs:
    cL.append(c)
    if c == 'C':
        break
print(cL)

# repeat
vs = itertools.repeat('A', 3)
vL = []
for v in vs:
    vL.append(v)
print(vL)

# chain
chains = itertools.chain('ABC', 'XYZ')
chainL = []
for chain in chains:
    chainL.append(chain)
print(chainL)

# groupby
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    nums = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    subNums = itertools.takewhile(lambda x: x <= 2*N-1, nums)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    cs = itertools.cycle([4, -4])
    numL = []
    for subNum in subNums:
        numL.append(next(cs) / subNum)
    # step 4: 求和:
    return sum(numL)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
