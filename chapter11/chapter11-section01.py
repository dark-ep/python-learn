#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 匹配
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切割字符串
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))


def is_valid_email(addr):
    # return re.match(r'^[a-zA-Z][a-zA-Z0-9.]+@[a-zA-Z0-9]+.com$', addr)
    return re.match(r'(^\w+)[.\w+]\w+@(\w+).(com$)', addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert not is_valid_email('.bob@example.com')
print('ok')


def name_of_email(addr):
    m = re.match(r'<?(\w+\s?\w+)>?.*@\w+.\w{3}', addr)
    return m.group(1)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
