# coding:utf-8
import yaml
import os
import requests
import json
import sys
sys.path.append("..")
from common import api_request
from params import yaml_handle

def test_get_meet_record_filelist():
    i=yaml_handle.read_yaml("cfgyaml.yaml")
    i=i[6] #6是获取会议录制文件列表
    i["request"]["json"]["confId"] = str(yaml_handle.read_yaml("responseyaml.yaml")["confId"])# 替换confId
    print(i)
    redata = api_request.api_request(i)
    return redata
    #request.check(redata,expectschema)

if __name__ == "__main__":
    test_get_meet_record_filelist()
