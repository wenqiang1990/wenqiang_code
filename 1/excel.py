#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd
data = xlrd.open_workbook('C:\\Users\\wenqiang.RFDOA\\Desktop\\yamaxun.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
list=[]
for i in range(nrows): # 循环逐行打印
    if i == 0: # 跳过第一行
        continue
    #print int(table.row_values(i)[3]) # 第四列
    list.append(int(table.row_values(i)[3]))
    #list.append('\n')
print list[0]
    