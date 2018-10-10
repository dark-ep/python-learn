#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取字符的整数表示
print(ord('A'))
print(ord('中'))

# 编码转换为对应的字符
print(chr(66))
print(chr(25991))

# 十六进制
print('\u4e2d\u6587')

# str->bytes
print(b'ABC')

# encode
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore'))

# len
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%04d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (s2 - s1) / s2 * 100
print('%.1f%%' % r)
