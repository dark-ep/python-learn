#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = lambda x: x * x
print(f)
print(f(5))


def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2)())

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
