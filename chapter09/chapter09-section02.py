#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# StringIO
from io import StringIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
from io import BytesIO

f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8', errors='ignore'))
