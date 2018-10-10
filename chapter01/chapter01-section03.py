#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

# 正序获取
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3]) # 数据越界

# 倒序获取
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# print(classmates[-4]) # 数据越界

# 插入数据
classmates.insert(1, 'Jack')  # 数据从0开始
print(classmates)

# 删除数据
print(classmates.pop())  # 删除最后一个
print(classmates)
print(classmates.pop(1))  # 删除指定索引
print(classmates)

# 类型处理
L = ['Apple', 123, True]
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']  # 多元数组
print(len(s))
print(s[2][0])
p = []
print(len(p))

# tuple
t = (1, 2)
print(t)
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])
