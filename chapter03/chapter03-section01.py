#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
l = list(range(100))
print(l)
print(l[:10])  # 前10个数
print(l[-10:])  # 后10个数
print(l[10:20])  # 前11~20的数
print(l[:10:2])  # 前10个数，每两个取一个
print(l[::5])  # 所有数，每五个取一个

t = tuple(range(100))
print(t)
print(t[:10])  # 前10个数
print(t[-10:])  # 后10个数
print(t[10:20])  # 前11~20的数
print(t[:10:2])  # 前10个数，每两个取一个
print(t[::5])  # 所有数，每五个取一个

s = 'ABCDEFG'
print(s[::2])  # 所有字符，每两个取一个
print(s[:3])  # 前3个字符


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
