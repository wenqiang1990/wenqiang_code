# -*- coding:utf-8 -*-
import pymysql
import contextlib
import requests
import json
import time
from bs4 import BeautifulSoup

config = {
    'host': '172.16.98.17',
    'port': 3306,
    'user': 'xin',
    'password': '48sdf37EB7',
    'db': 'xin_cash_loan',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
url = 'http://develop.sapi.rmb.test.youxinjinrong.com/in_loan/bank_card/list'
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


def s_status(order_id):
    with connect_mysql() as cursor:
        sql = "select order_num,status from cash_order where id = " + str(order_id) + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results


def s_cash_trade_flow(order_num):
    with connect_mysql() as cursor:
        sql = "select status from cash_trade_flow where order_num = '" + order_num + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results


def update_cash_order(order_id):
    with connect_mysql() as cursor:
        sql = "update cash_order set status = 4 WHERE id = " + str(order_id) + ";"
        cursor.execute(sql)


def bank_card(cuser_id):
    params = {'cuser_id': cuser_id, 'debug': 1}
    try:
        res = requests.get(url, params=params)
        bank_card_id = json.loads(res.text)['data'][0]['id']
        return bank_card_id
    except Exception:
        return 0


def post_info():
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


if __name__ == "__main__":
    # 1590202657
    cuser_id = 915884
    bank_card_id = bank_card(cuser_id)
    if bank_card_id == 0:
        print ('bank_card请求异常')
    else:
        order_id = to_loan(cuser_id, bank_card_id)
        if order_id == 0:
            print('bank_card请求异常')
    if isinstance(order_id, int):
        update_cash_order(order_id)
        for i in range(0, 30):
            results = s_status(order_id)
            status = results[0]['status']
            order_num = results[0]['order_num']
            if status == 6:
                break
            else:
                print ('cash_order状态不为6,10秒后继续查询')
                time.sleep(10)
                continue
        code = post_info()
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
                break
            elif fin_status == -1:
                print ('放款失败')
                break
    else:
        print (order_id)
