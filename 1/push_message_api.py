# coding:utf-8
import yaml
import os
import requests
import json


#print(cfg)
#cfg = json.dumps(cfg)
def api_request(i):
    for m in range(i):
        method = 'POST'
        url = "http://192.168.179.160:8021/2015-05-18/Corp/yuntongxun/Push/Message"
        headers = {"Content-Type": "application/json;charset=utf-8"}
        data = "{\"appId\":\"ff8080815dbc080c015dbc9d7cd40003\",\"pushType\":\"1\",\"sender\":\"13366778610\",\"receiver\":[\"13366778612\"],\"msgType\":\"1\",\"msgContent\":%s,\"msgFileUrl\":\"\",\"msgFileName\":\"\",\"msgDomain\":\"\"}" %m
        print(type(headers))
        response = requests.request(method, url, headers=headers, data=data)
        #print(r.text)
        print(response.json())
        #print(json.loads(r.text))

api_request(1)