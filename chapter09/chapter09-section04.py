#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = dict(name='Bob', age=20, score=88)

# 二进制序列化反序列化
import pickle

# 序列化
# dByte = pickle.dumps(d)
# print(dByte)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
# print(pickle.loads(dByte))
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# Json序列化反序列化
import json

# 序列化
jsonStr = json.dumps(d)
print(jsonStr, type(jsonStr))

# 反序列化
d = json.loads(jsonStr)
print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
sJson = json.dumps(s, default=lambda obj: obj.__dict__)
print(sJson)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(sJson, object_hook=dict2student))

# 转义成ascii
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
