# -*- coding: utf-8 -*-
#操作手册：https://www.cnblogs.com/xuchunlin/p/7061524.html
#redis安装：https://blog.csdn.net/chivalrousli/article/details/77842670  pip install Redis

import excute

import redis
#这个redis 连接不能用，请根据自己的需要修改
r =redis.Redis(host="172.16.98.10",port=6379)
'''Redis使用说明：
>>> r.set('12345', '3d57228d760a93')
True
>>> r.get('1')获取value值
b'4028b2883d3f5a8b013d57228d760a93'
>>> r.exists('1')存在就返回True
1
>>> r.exists('2')不存在就返回False
0
'''
def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
	
#获取order_num
excute.makeloanflow()
key1='sapi.rmb.jr:loan_flow_five_limit'+order_num#5分钟内重复生成流水限制
value1=r.get('key1')
signal1=r.exists('key1')
if signal1 = 1:
    print('生成流水1次，已计入Redis缓存！key值为(%s)'%value1)
else
    print('生成流水1次，未计入Redis缓存！')

excute.makeloan()
key2='sapi.rmb.jr:loan_make_loan_count'+order_num#向渠道请求放款
value2=r.get('key2')
if value2 is not None:
    print('向渠道请求放款1次，已计入Redis缓存！key值为(%s)'%value2)
else
    print('向渠道请求放款1次，未计入Redis缓存！')

r.get('key1') 
r.exists('2')
