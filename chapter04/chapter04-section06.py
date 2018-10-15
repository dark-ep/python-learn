#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()
print(now.__name__)  # wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)  # wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
print(now.__name__)  # now
