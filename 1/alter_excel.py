# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlrd import open_workbook
#https://www.cnblogs.com/yanhuidj/p/9011870.html 操作
'''
#使用xlrd读取指定excel工作中的指定表格的值并返回 xlrd是用来从Excel中读写数据的，但我平常只用它进行读操作，写操作会遇到些问题
#打开excel文件
data=xlrd.open_workbook('D:\\会议直播录像功能测试用例.xls')
#获取第一张工作表（通过索引的方式）
table=data.sheets()[0]
#data_list用来存放数据
data_list=[]
#将table中第一行的数据读取并添加到data_list中
data_list.extend(table.row_values(0))
#data_list.extend(table.column_values(0))#第一列
#打印出第一行的全部数据
for item in data_list:
    print(item)
#通过循环读取表格的所有行
for rownum in range(table.nrows):
    print(table.row_values(rownum))

#获取单元格的值
cell_A1=table.row(0)[1].value
print(cell_A1)
#或者像下面这样
cell_A1=table.cell(1,0).value
print(cell_A1)
#或者像下面这样通过列索引
cell_A1=table.col(1)[1].value
print(cell_A1)
'''
#新建一个Excel文件（只能通过新建写入）
data1=xlwt.Workbook()
#新建一个表
table=data1.add_sheet('name')
#写入数据到A1的单元格
#table.write(0,0,u'呵呵')
#如果对同一个单元格重复操作，会引发overwrite Exception，想要取消该功能，需要在添加工作表时指定为可覆盖，像下面这样
#table=data1.add_sheet('name',cell_overwrite_ok=True)


#初始化样式
style=xlwt.XFStyle()
#为样式创建字体
font=xlwt.Font()
#指定字体名字
font.name='Times New Roman'
#字体加粗
font.bold=True
#将该font设定为style的字体
style.font=font
#写入到文件时使用该样式
table.write(0,2,'just for test',style)
#保存文件
data1.save('D:\\test.xls')

