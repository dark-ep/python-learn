#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 自定义 isinstance
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# print(my_abs('x'))

# pass
def nop():
    pass  # 占位符


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    # ax2 + bx + c = 0
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type')
    delta = b * b - 4 * a * c
    if a == 0:
        x = -c / b
        return x
    elif delta < 0:
        print('此方程无解')
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x1 = x2 = -b / 2 * a
        return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
