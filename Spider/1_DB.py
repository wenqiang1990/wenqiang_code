# -*- coding:utf-8 -*-
import pymysql
import contextlib
import requests
import json
import time
from bs4 import BeautifulSoup

#打开数据库连接
db= pymysql.connect(host="192.168.179.145",user="openser",
 	password="yanshiopenserpass92",db="wenqiang_test",port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql1 = "INSERT INTO redmine (name, time ,bug_number,parent_task) VALUES ('球球','20190117','2174','111');"
sql2 = "select * from redmine"
sql3 = 'alter table redmine change id id int auto_increment'
try:
    # 执行sql语句
	cur.execute(sql1)
	## 提交到数据库执行
	db.commit()
except Exception as e:
	#错误回滚
	print(db.rollback())
finally:
	db.close()
'''
db= pymysql.connect(host="192.168.179.145",user="openser",
 	password="yanshiopenserpass92",db="wenqiang_test",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()
try:
    cur.execute(sql2)  # 执行sql语句
    results = cur.fetchall()  # 获取查询的所有记录
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
'''


