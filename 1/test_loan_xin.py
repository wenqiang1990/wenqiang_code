# -*- coding:utf-8 -*-
import pymysql
import contextlib
import requests
import json
import time

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
url_login = 'http://sso.ceshi.youxinjinrong.com/api/checklogin'


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
    headers_login = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'uid=rBBiElvzwLIC8B3iA42PAg==; NSC_eqppmuftu.yjo.dpn=ffffffffaf187c0345525d5f4f58455e445a4a423660; testing_newsso_token=134cd8091bb2b3e5ced1bf6a818852c6abd3f2a7',
        'Content - Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'sso.ceshi.youxinjinrong.com',
        'Referer': 'http://sso.ceshi.youxinjinrong.com/api/login?refer=http://cron.ceshi.youxinjinrong.com/crontab/index/?crontab%2Findex%2F=&creator=huangwei&page=2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data_login = {'username': 'lichunxiao',
                  'pwd': 'XIA987654321!',
                  'refer': 'http://cron.ceshi.youxinjinrong.com/crontab/index/?crontab/index/='}
    res1 = requests.post(url_login, data=data_login, headers=headers_login)
    testing_newsso_token = res1.cookies['testing_newsso_token']
    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'uid=rBBiElvzwLIC8B3iA42PAg==; PHPSESSID=sos4ggcgsok44lfoiev8823890; NSC_eqppmuftu.yjo.dpn=ffffffffaf187c0345525d5f4f58455e445a4a423660; testing_newsso_token=' + testing_newsso_token,
        'Content - Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'cron.ceshi.youxinjinrong.com',
        'Referer': 'http://cron.ceshi.youxinjinrong.com/crontab/index/?crontab%2Findex%2F=&creator=huangwei&page=2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        res = requests.post(url_post, data=data, headers=headers)
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
            print ('bank_card请求异常')
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
            print ('脚本执行成功！')
        else:
            print ('脚本执行失败！')
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
