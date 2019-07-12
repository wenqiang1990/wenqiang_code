#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='123.57.140.180',
        port = 3306,
        user='yoya',
        passwd='yoya123456',
        db ='yoyamobile',
        )
cur = conn.cursor()

#修改查询条件的数据
cur.execute("update yoyo_ki set status= 1 where ID = 16")
print u"将国际流量库存调整为1"
#修改查询条件的数据
cur.execute("update yoyo_goods set status= 1 where ID = 1")
print u"将商品“香港5日套餐”改为上架状态"
cur.execute("update yoyo_goods set status= 1 where ID = 8")
print u"将商品“印度尼西亚10日流量包”改为上架状态"
cur.execute("update yoyo_goods set status= 1 where ID = 12")
print u"将商品“日本7日套餐”改为上架状态"
cur.execute("update yoyo_goods set status= 1 where ID = 14")
print u"将商品“香港7天卡”改为上架状态"



#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()