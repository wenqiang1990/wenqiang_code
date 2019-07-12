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
    i=i[3] #3是开始会议录制配置项
    #i["request"]["json"]["confId"] = str(yaml_handle.read_yaml("responseyaml.yaml")["confId"])# 替换confId
    redata = api_request.api_request(i)
    n=redata["recordData"][0] #取出sessionid
    yaml_handle.write_a_yaml("responseyaml.yaml",n)
    return redata
    #request.check(redata,expectschema)

if __name__ == "__main__":
    test_stop_meet_record()
