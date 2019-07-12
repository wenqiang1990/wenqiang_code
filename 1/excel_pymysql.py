# -*- coding: utf-8 -*-
import xlrd
import pymysql
import re

conn = pymysql.connect(host='database connect address', port=1234, user='root',
                       passwd='****', db='database name', charset='utf8mb4')
p = re.compile(r'\s')
data = xlrd.open_workbook('./W020170616379651135432.xls')
table = data.sheets()[0]
t = table.col_values(1)
nrows = table.nrows
ops = []
for i in range(nrows):
    r1 = table.row_values(i)
    if len(r1[2]) == 10:
        ops.append((r1[2], p.sub('', r1[1]), p.sub('', r1[3]), p.sub('', r1[4]), r1[5], r1[6]))

cur = conn.cursor()
cur.executemany('insert into `university_copy` (`id`, `name`, `ministry`, `city`, `level`, `memo`) \
     values (%s, %s, %s, %s, %s, %s)', ops)
conn.commit()
cur.close()

conn.close()