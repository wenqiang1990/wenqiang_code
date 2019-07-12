# -*- coding:utf-8 -*-
import requests,re,json, urllib
import hashlib
import sys
import xlrd
import time
import os


reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()

# vin = 'LDC703L29A0239394'
appver = '3.7.110'
mobile = '15899951234'
key = 'm1K5@BcxUn!'
url_login = 'http://resume37.api.ceshi.xin.com/resume/r_user/login'
url_create_order = 'http://resume37.api.ceshi.xin.com/resume/r_resume_action/create_order'
url_send_smscode = 'http://resume37.api.ceshi.xin.com/resume/r_user/send_smscode'
url_vin_query = 'http://resume37.api.ceshi.xin.com/resume/r_resume_action/vin_query'
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}


# data_send_smscode = {
#     '_apikey': 'fcc48e',
#     'app_source': 19,
#     'appver': appver,
#     'cityid': 201,
#     'imei': '868029020304762',
#     'mobile': mobile,
#     'nb': 'NBCUFQRO99999999',
#     'os': 'android',
#     'rtoken': '',
#     'token': ''
# }
def load_to_excel():
    file_name = 'list_vin.xlsx'
    #打开Excel文件读取数据
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_name('Sheet1')
    list_vin = []
    for r in range(1, sheet.nrows):
        vin = sheet.cell(r, 0).value
        vin_format = format_vin(vin)
        list_vin.append(vin_format)
    return list_vin

def format_vin(vin):
    if '\t' in vin:
        vin = vin.replace('\t', '')
    if '\n' in vin:
        vin = vin.replace('\n', '')
    return vin

def make_apikey(key, data):
    # _apikey = urllib.quote(data)
    # api_key = urllib.urlencode(data) + key
    api_key = data + key
    apikey = md5_encode(api_key)
    _apikey = apikey[20] + apikey[15] + apikey[0] + apikey[3] + apikey[1] + apikey[5]
    return _apikey


def md5_encode(key):
    m = hashlib.md5()
    m.update(key)
    return m.hexdigest()


def send_smscode():
    data_send_smscode = 'app_source=19&appver=' + appver + '&cityid=201&imei=868029020304762&mobile=' + mobile + '&nb=NBCUFQRO99999999&os=android&rtoken=&token='
    apikey = make_apikey(key, data_send_smscode)
    # data_send_smscode.update(_apikey=apikey)
    data_send_smscode += '&_apikey=' + apikey
    res_ss = requests.post(url_send_smscode, data=data_send_smscode, headers=headers)
    print res_ss.text
    p1 = re.compile(r'\d:(.*?)"')
    captcha = p1.findall(res_ss.text)
    if captcha:
        return captcha[0]
    else:
        if json.JSONDecoder().decode(res_ss.text)['code'] == -1:
            print '手机号有误!'
            return -1
        else:
            print "超过每日次数限制"
            return 0
            # print res2.text


def login(captcha):
    # data_login = {
    #     'app_source': 19,
    #     'appver': appver,
    #     'cityid': 201,
    #     'imei': '868029020304762',
    #     'mobile': mobile,
    #     'nb': 'NBCUFQRO99999999',
    #     'os': 'android',
    #     'rtoken': '8d0f1e6e2d682183a51e0c55a9670ae0',
    #     'smscode': captcha,
    #     'token': '8d0f1e6e2d682183a51e0c55a9670ae0'
    # }
    data_login = 'app_source=19&appver=' + appver + '&cityid=201&imei=868029020304762&mobile=' + mobile + '&' \
                                                                                                          'nb=NBCUFQRO99999999&os=android&rtoken=&smscode=' + captcha + '&token='
    apikey = make_apikey(key, data_login)
    # data_login.update(_apikey=apikey)
    data_login += '&_apikey=' + apikey
    res_login = requests.post(url_login, data=data_login, headers=headers)

    if eval(res_login.text)['code'] == 2:
        token = eval(res_login.text)['data']['rtoken']
        userid = eval(res_login.text)['data']['userid']
        print res_login.text
        return token
    elif eval(res_login.text)['code'] == -1:
        print res_login.text
        return eval(res_login.text)['message']
    else:
        print res_login.text
        return eval(res_login.text)['message']


def vin_query(token):
    # data_vin_query = {
    #     'app_source': 19,
    #     'appver': appver,
    #     'cityid': 201,
    #     'imei': '868029020304762',
    #     'nb': 'NBCUFQRO99999999',
    #     'os': 'android',
    #     'rtoken': token,
    #     'token': token,
    #     'vin': vin}
    data_vin_query = 'app_source=19&appver=' + appver + '&cityid=201&imei=868029020304762&nb=NBCUFQRO99999999&' \
                                                        'os=android&rtoken=' + token + '&token=' + token + '&vin=0019B01347NK4G73D'
    apikey = make_apikey(key, data_vin_query)
    # data_vin_query.update(_apikey=apikey)
    data_vin_query += '&_apikey=' + apikey
    res_vq = requests.post(url_vin_query, data=data_vin_query, headers=headers)
    print res_vq.text
    if eval(res_vq.text)['code'] == 2:
        return 1
    else:
        return 0


def create_order(token, vin):
    # data_create_order = {
    #     'app_source': 19,
    #     'appver': appver,
    #     'brandid': 71,
    #     'cityid': 201,
    #     'create_type': 1,
    #     'engineid': '',
    #     'imei': '868029020304762',
    #     'nb': 'NBCUFQRO99999999',
    #     'os': 'android',
    #     'rtoken': token,
    #     'token': token,
    #     'vin': vin}
    data_create_order = 'app_source=19&appver=' + appver + '&brandid=135&cityid=201&create_type=1&engineid=&' \
                                                           'imei=868029020304762&nb=NBCUFQRO99999999&os=android&rtoken=' + token + '&token=' + token + '&' \
                                                                                                                                                       'vin=' + vin
    apikey = make_apikey(key, data_create_order)
    # data_create_order.update(_apikey=apikey)
    data_create_order += '&_apikey=' + apikey
    res_co = requests.post(url_create_order, data=data_create_order, headers=headers)
    print res_co.text
    if eval(res_co.text)['code'] == 2:
        orderid = eval(res_co.text)['data']['orderid']
        return 1
    else:
        return eval(res_co.text)['message']


if __name__ == "__main__":
    list_vin = load_to_excel()
    captcha = send_smscode()
    if captcha == 0:
        print "超过每日次数限制"
    elif captcha == -1:
        print '手机号有误!'
    else:
        token = login(captcha)
        if token.isalnum():
            for i in range(0, len(list_vin)):
                result_co = create_order(token, list_vin[i])
                if result_co == 1:
                    print '下单成功！VIN为：' + list_vin[i]
                    time.sleep(6)
                else:
                    print '下单失败！VIN为：' + list_vin[i] + ',' + result_co.decode('unicode_escape')

        else:
            print '登录失败！' + token.decode('unicode_escape')
    print 'Done!'
