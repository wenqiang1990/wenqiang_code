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
    i = i[2]  # 2是停止直播
    redata = api_request.api_request(i)
    return redata
    # request.check(redata,expectschema)

if __name__ == "__main__":
    test_start_meet_living()

