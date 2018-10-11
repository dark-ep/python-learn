#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# insert
d['Adam'] = 67
print(d['Adam'])

# repeat insert
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# null
print('Thomas' in d)  # False

# get
print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))

# pop
print(d.pop('Bob'))
print(d)

# set
s = set([1, 1, 2, 2, 3, 3])
print(s)

# add
s.add(4)
print(s)
s.add(4)
print(s)

# remove
s.remove(4)
print(s)

# & |
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# sort
a = ['c', 'b', 'a']
a.sort()
print(a)

# replace
a = 'abc'
print(a.replace('a', 'A'))
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

# “tuple一旦初始化就不能修改” ==  tuple一旦初始化 元素地址不可变，但是值（对象）可变，
t1 = (1, 2, 3)
t2 = (1, [2, 3])
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
d[t1] = 'value'
# d[t2] = 'value'
s1 = set(t1)
# s2 = set(t2)
