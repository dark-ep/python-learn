#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数
def fact1(n):
    if n == 1:
        return 1
    return n * fact2(n - 1)


print(fact1(1))
print(fact1(5))


# print(fact(1000)) # 堆栈溢出


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact2(1))
print(fact2(5))


# 汉诺塔的移动可以用递归函数非常简单地实现。
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
