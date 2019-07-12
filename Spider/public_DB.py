# -*- coding:utf-8 -*-
import pymysql
import contextlib
import requests
import json
import time
from bs4 import BeautifulSoup

config = {
    'host': '192.168.177.116',
    'port': 3306,
    'user': 'root',
    'password': '121518',
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
'''直接从数据库取id'''
def bank_card_id(cuser_id):
    with connect_mysql() as cursor:
        sql = "select id from cash_user_card where is_using = 1 and cuser_id = " + str(cuser_id) + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results

def order(id):
    with connect_mysql() as cursor:
        sql = "select order_num,loan_money,status from cash_order where id = " + str(id) + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
    return results



