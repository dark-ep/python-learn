#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>#

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

height = 1.75
weight = 80.5
bmi = weight / pow(height, 2)  # BMI公式（体重除以身高的平方）
print('BMI指数是%.2f' % bmi)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
elif bmi >= 32:
    print('严重肥胖')
