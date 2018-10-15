#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):  # __init__方法的第一个参数永远是self
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
lisa.print_score()
bart.print_score()
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

bart.age = 8
print(bart.age)
# print(lisa.age)
