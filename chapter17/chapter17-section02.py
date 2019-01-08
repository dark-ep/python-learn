#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import mysql.connector

# 初始数据:
conn = mysql.connector.connect(
    user='oper', password='oper', host='192.168.159.131', port='3306', database='test')
cursor = conn.cursor()
cursor.execute(
    'drop table if exists user')
cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute('insert into user (id, name, score) values (%s, %s, %s)', [
    'A-001', 'Adam', 95])
cursor.execute('insert into user (id, name, score) values (%s, %s, %s)', [
    'A-002', 'Bart', 62])
cursor.execute('insert into user (id, name, score) values (%s, %s, %s)', [
    'A-003', 'Lisa', 78])
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):  # 返回指定分数区间的名字，按分数从低到高排序
    try:
        conn = mysql.connector.connect(
            user='oper', password='oper', host='192.168.159.131', port='3306', database='test')
        try:
            cursor = conn.cursor()
            cursor.execute(
                'select name from user where score between %s and %s order by score', (low, high))
            values = cursor.fetchall()
            names = [v[0] for v in values]
            return names
        finally:
            cursor.close()
        conn.commit()
    finally:
        conn.close()


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
