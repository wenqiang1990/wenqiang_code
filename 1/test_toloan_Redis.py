# -*- coding:utf-8 -*-
import pymysql
import contextlib
import requests
import json
import time
from bs4 import BeautifulSoup

import redis
#这个redis 连接不能用，请根据自己的需要修改
r =redis.Redis(host="172.16.98.10",port=6379)

import hashlib
def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

config = {
    'host': '172.16.98.17',
    'port': 3306,
    'user': 'xin',
    'password': '48sdf37EB7',
    'db': 'xin_cash_loan',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

url_to_loan = 'http://develop.rmbfapi.test.youxinjinrong.com/in_loan/to_loan'
url_post = 'http://cron.ceshi.youxinjinrong.com/crontab/execute'
url_login = 'http://sso.ceshi.youxinjinrong.com/login/login'


@contextlib.contextmanager
def connect_mysql():
    conn = pymysql.connect(**config)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

'''订单表状态'''
def s_status(order_id):
    with connect_mysql() as cursor:
        sql = "select order_num,status from cash_order where id = " + str(order_id) + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results
'''流水表状态'''
def s_cash_trade_flow(order_num):
    with connect_mysql() as cursor:
        sql = "select status from cash_trade_flow where order_num = '" + order_num + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results

'''订单状态置为4'''
def update_cash_order(order_id):
    with connect_mysql() as cursor:
        sql = "update cash_order set status = 4 WHERE id = " + str(order_id) + ";"
        cursor.execute(sql)

		
'''直接从数据库取id'''
def bank_card_id(cuser_id):
    with connect_mysql() as cursor:
        sql = "select id from cash_user_card where is_using = 1 and cuser_id = " + str(cuser_id) + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results



'''下单接口'''
def to_loan(cuser_id, bank_card_id):
    params = {'cuser_id': cuser_id, 'loan_period': 3, 'loan_money': 5000, 'product_id': 1, 'bank_card_id': bank_card_id,
              'debug': 1}
    try:
        res = requests.get(url_to_loan, params=params)
        data = json.loads(res.text)['data']
        if data is None:
            msg = json.loads(res.text)['msg']
            return msg
        order_id = json.loads(res.text)['data']['order_id']
        print ('order_id为%s' % order_id)
        return order_id
    except Exception:
        return 0
'''放款脚本'''		
def post_info():
    data = {'id': 3217887331484697062}
    r1 = requests.get('http://sso.ceshi.youxinjinrong.com/login/index')
    soup = BeautifulSoup(r1.text)
    cookies1 = r1.cookies
    token1 = soup.find(id="csrf_token")["value"].encode('utf-8')
    data_login = {'username': 'lichunxiao',
                  'pwd': 'XIAO987654321@',
                  '_token': token1}
    r2 = requests.post(url_login, data=data_login, cookies=cookies1 )

    cookies2 = r2.cookies.get_dict()
    try:
        res = requests.post(url_post, data=data, cookies=cookies2)
        return res.text
    except Exception:
        return 0

def post_info2():
    data = {'id': 3217887726271463431}
    r1 = requests.get('http://sso.ceshi.youxinjinrong.com/login/index')
    soup = BeautifulSoup(r1.text)
    cookies1 = r1.cookies
    token1 = soup.find(id="csrf_token")["value"].encode('utf-8')
    data_login = {'username': 'lichunxiao',
                  'pwd': 'XIAO987654321@',
                  '_token': token1}
    r2 = requests.post(url_login, data=data_login, cookies=cookies1 )

    cookies2 = r2.cookies.get_dict()
    try:
        res = requests.post(url_post, data=data, cookies=cookies2)
        return res.text
    except Exception:
        return 0
def post_info3():
    data = {'id': 3217887985447993377}
    r1 = requests.get('http://sso.ceshi.youxinjinrong.com/login/index')
    soup = BeautifulSoup(r1.text)
    cookies1 = r1.cookies
    token1 = soup.find(id="csrf_token")["value"].encode('utf-8')
    data_login = {'username': 'lichunxiao',
                  'pwd': 'XIAO987654321@',
                  '_token': token1}
    r2 = requests.post(url_login, data=data_login, cookies=cookies1 )

    cookies2 = r2.cookies.get_dict()
    try:
        res = requests.post(url_post, data=data, cookies=cookies2)
        return res.text
    except Exception:
        return 0


if __name__ == "__main__":
    # 1590202657、5425450
    cuser_id =915884
    bank_card_id1 = bank_card_id(cuser_id)
    bank_card_id = bank_card_id1[0]['id']
    if bank_card_id == 0:
        print ('bank_card1111请求异常')
    else:
        print(bank_card_id)
        order_id = to_loan(cuser_id, bank_card_id)
        if order_id == 0:
            print('bank_card22222请求异常')
    if isinstance(order_id, int):
        update_cash_order(order_id)
        for i in range(0, 30):
            results = s_status(order_id)
            status = results[0]['status']
            order_num = results[0]['order_num']

        '''生成流水'''
        
        code = post_info()
        if json.loads(code)['code'] == 0:
            print('生成流水脚本第一次执行成功！')

            for i in range(0, 30):
                results = s_status(order_id)
                status = results[0]['status']
                if status == 4:
                    print ('订单状态为4,10秒后重新查询')
                    time.sleep(10)
                    continue
                if status == 6:
                    print('第一次输出状态(%s)'%status)#第一次输出
                    break

            update_cash_order(order_id)
            
            results = s_status(order_id)
            status = results[0]['status']

            time.sleep(60)
            print('第二次输出状态(%s)'%status)#第二次输出
    
            code = post_info()
            if json.loads(code)['code'] == 0:
                print('生成流水脚本第二次执行成功！')
                results = s_status(order_id)
                status = results[0]['status']
                print(status)#第三次输出
            else :
                print('生成流水脚本第二次执行失败!')
            
            
            key1='sapi.rmb.jr:loan_flow_five_limit:'+order_num #5分钟内重复生成流水限制
            print(key1)
            valuel1=r.get(key1).decode('utf-8')
            print(valuel1)
            #signal1=r.exists(key1)
            if valuel1 is not None:
                print('生成流水1次，已计入Redis缓存！key值为(%s)'%valuel1)
            else:
                print('生成流水1次，未计入Redis缓存！')
        else:
            print('脚本执行失败！')

        '''放款'''
        code = post_info2()
        if json.loads(code)['code'] == 0:
            print('脚本执行成功！')

            for i in range(0, 30):
                fin_status = s_cash_trade_flow(order_num)[0]['status']
                if fin_status == 3:
                    print ('流水状态为3,10秒后重新查询')
                    time.sleep(10)
                    continue
                if status == 4:
                    print('第一次输出流水状态(%s)'%fin_status)#第一次输出流水状态
                    break
                
            key2=md5('sapi.rmb.jr:loan_make_loan_count'+order_num)#向渠道请求放款
            print(key2)
            
        else:
            print('脚本执行失败！')
			
        code = post_info3()
        if json.loads(code)['code'] == 0:
            print('脚本执行成功！')	
        else:
            print('脚本执行失败！')			
		
        for i in range(0, 30):
            fin_status = s_cash_trade_flow(order_num)[0]['status']
            if fin_status == 4:
                print ('cash_trade_flow状态为4,10秒后重新查询')
                time.sleep(10)
                continue
            if fin_status == 2:
                print ('放款成功')
                
                valuel2=r.get(key2).decode('utf-8')
                print(valuel2)
                if valuel2 is not None:#只有放款成功的才会返回key-value
                    print('向渠道请求放款1次，已计入Redis缓存！key值为(%s)'%valuel2)
                else:
                    print('向渠道请求放款1次，未计入Redis缓存！')
                    
                break
            elif fin_status == -1:
                print ('放款失败')
                valuel2=r.get('key2')
                print(valuel2)
                if valuel2 is  None:
                    print('向渠道请求放款失败，Redis缓存已清空！')
                break
    else:
        print (order_id)
