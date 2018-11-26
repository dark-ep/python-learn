#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


from urllib import request

class MySaxHandler(object):
    def __init__(self):
        self.result = dict(city=None, forecast=[])
    def start_element(self, name, attr):
        if attr.get("city"):
            self.result["city"] = attr["city"]
        if attr.get("date") and not attr.get("temp"):
            self.result["forecast"].append(dict(date=attr["date"], high=attr["high"], low=attr["low"]))

def parseXml(xml_str):
    parser = ParserCreate()
    handler = MySaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)
    return handler.result

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('ok')