# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

baseUrl = 'http://sso.ceshi.youxinjinrong.com/'

r1 = requests.get(baseUrl + 'login/index')

soup = BeautifulSoup(r1.text)

cookies = r1.cookies
token = soup.find(id="csrf_token")["value"].encode('utf-8')

r2 = requests.post(baseUrl + 'login/login', data={"username":"lichunxiao", "pwd":"XIAO987654321!", "_token":token},
                   cookies=cookies)

cookie2 = r2.cookies.get_dict()
#r3 = requests.get('http://cron.ceshi.youxinjinrong.com/', cookies=cookie2)

r4=requests.post('http://cron.ceshi.youxinjinrong.com/crontab/execute',data={'id': 3217887726271463431},cookies=cookie2)
print(r4.text)
