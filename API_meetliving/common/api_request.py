# coding:utf-8
import yaml
import os
import requests
import json
import schema
import jsonschema
import sys
sys.path.append("..")
from params import schema2
from jsonschema import validate

#print(cfg)
#cfg = json.dumps(cfg)
def api_request(i):
    request = i["request"]
    name = i["name"]
    print(name)
    method = request["method"]
    url = request["url"]
    headers = request["headers"]
    data = json.dumps(request["json"])#json.dumps字典转json
    response = requests.request(method,url,headers=headers,data=data)
    #print(r.text)
    print(response.json())
    #print(json.loads(r.text))
    return response.json()#与schema做格式比较需要转成json格式

def check(redata,expectschema):
    status=redata["statusCode"]
    if status == '000000':
        try:
            validate(redata, expectschema)
            print("schema格式验证通过")
        except jsonschema.ValidationError as ex:
            msg = ("HTTP response body is invalid (%s)") % ex
            #raise exceptions.InvalidHTTPResponseBody(msg)
            print("msg = %" %msg)
    else:
        print("请求失败")

#redata=api_request(2)
#check(redata)


