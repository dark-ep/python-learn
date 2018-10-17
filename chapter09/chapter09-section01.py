#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# try:
#     f = open('E:\\test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
with open('E:\\test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

with open('E:\\568a407c950fd6a61e835.jpg', 'rb') as f:
    print(f.read())

with open('E:\\gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

with open('E:\\test.txt', 'w') as f:
    f.write('Hello, world![w]')

with open('E:\\test.txt', 'a') as f:
    f.write('Hello, world![a]')
