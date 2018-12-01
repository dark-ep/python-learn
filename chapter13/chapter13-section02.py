#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.douban.com/')  # 豆瓣首页
print(r.status_code)
print(r.text)

r = requests.get('https://www.douban.com/search',
                 params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print(r.content)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
params = {'key': 'value'}
r = requests.post('https://www.douban.com/', json=params) # 内部自动序列化为JSON

upload_files = {'file': open('report.xls', 'rb')}
r = requests.post('https://www.douban.com/', files=upload_files)

print(r.headers['Content-Type'])
print(r.cookies['ts'])


cs = {'token': '12345', 'status': 'working'}
r = requests.get('https://www.douban.com/', cookies=cs)

r = requests.get('https://www.douban.com/', timeout=2.5) # 2.5秒后超时
