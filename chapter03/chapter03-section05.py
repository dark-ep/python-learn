#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可迭代对象
from collections.abc import Iterable

print(isinstance([], Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  # True
print(isinstance(100, Iterable))  # False

# 迭代器
from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))  # True
print(isinstance([], Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance('abc', Iterator))  # False
print(isinstance(iter([]), Iterator))  # True
print(isinstance(iter('abc'), Iterator))  # True
