# coding:utf-8
import yaml
import os
import requests
import json
import sys
sys.path.append("..")
from common import api_request
from params import yaml_handle

def test_stop_meet_record():
    i=yaml_handle.read_yaml("cfgyaml.yaml")
    i=i[5] #5是停止会议录制
    #i["request"]["json"]["sessionId"]=yaml_handle.read_yaml("responseyaml.yaml")["sessionId"]#替换sessionid
    #i["request"]["json"]["confId"] = str(yaml_handle.read_yaml("responseyaml.yaml")["confId"])  # 替换confId str
    print(i)
    redata = api_request.api_request(i)
    return redata
    #request.check(redata,expectschema)

if __name__ == "__main__":
    test_stop_meet_record()



