#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


# 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


# logging
import logging

logging.basicConfig(level=logging.INFO)  # debug，info，warning，error


def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

# pdb 调试
