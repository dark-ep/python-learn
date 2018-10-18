#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)  # b'\x00\x9c@c'

import struct

print(struct.pack('>I', 10240099))

print(struct.unpack('>IH',
                    b'\xf0\xf0\xf0\xf0\x80\x80'))  # https://docs.python.org/3/library/struct.html#format-characters

import base64

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
#
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数

# 可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
def bmp_info(data):
    info = struct.unpack('<ccIIIIIIHH', data[:30])
    if info[0] == b'B' and info[1] == b'M':
        return {
            'width': info[6],
            'height': info[7],
            'color': info[-1]
        }
    else:
        print('不是位图文件')


# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
