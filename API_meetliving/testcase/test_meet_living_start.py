# coding:utf-8
import yaml
import os
import requests
import json
import sys
import unittest
sys.path.append("..")
from common import api_request
from params import yaml_handle

def test_start_meet_living():
    i = yaml_handle.read_yaml("cfgyaml.yaml")
    i = i[0]  # 0是开始直播
    redata = api_request.api_request(i)
    return redata
    n=i[request][json][confId]
    yaml_handle.write_w_yaml("responseyaml.yaml", n) # 将yaml中第一项会议id 写入返回yaml文件，
    # request.check(redata,expectschema)

if __name__ == "__main__":
    test_start_meet_living()

