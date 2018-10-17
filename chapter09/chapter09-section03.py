#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 操作系统信息
print(os.name)
# print(os.uname()) # uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

# 操作文件和目录
print(os.path.abspath('.'))
p = os.path.join('E:', 'testdir')
os.mkdir(p)  # 创建一个目录:
os.rmdir(p)  # 删掉一个目录:
print(os.path.split('E:\gbk.txt'))
print(os.path.splitext('E:\gbk.txt'))
with open('E:\\test.txt', 'w') as f:
    f.write('Hello, world![w]')
os.rename('E:\\test.txt', 'E:\\test.py')  # 对文件重命名
os.remove('E:\\test.py')  # 删除文件

print([x for x in os.listdir('E:\\') if os.path.isdir(os.path.join('E:\\', x))])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


def findFile(path, key):
    path = os.path.abspath(path)  # 绝对路径
    try:
        fs = os.listdir(path)  # 遍历
        for f in fs:  # 文件目录名称
            fullpath = os.path.join(path, f)  # 完整目录
            if os.path.isdir(fullpath):
                findFile(fullpath, key)
            elif f.find(key) != -1:
                print(os.path.join(path, f))
    except WindowsError:
        print("Oops - we're not allowed to list %s" % path)


findFile('E:\\Work\\py-learn', 'chapter09')
