# coding:utf-8
import json
import sys
sys.path.append("..")
from common import api_request
from params import yaml_handle
from common import globle_set

def test_start_meet_living():
    i = yaml_handle.read_yaml("cfgyaml.yaml")
    i = i[0]  # 0是开始直播
    redata = api_request.api_request(i)
    global confId ,sessionId
    confId = i["request"]["json"]["confId"]    #取会议id
    sessionId = redata["liveData"][0]["sessionId"]  # 取出sessionid
    #print("sessionid = %s" %sessionId)
    globle_set.set_map("confId", confId)
    globle_set.set_map("sessionId", sessionId)
    assert redata["statusCode"] == "000000"
    return confId,sessionId
    #yaml_handle.write_w_yaml("responseyaml.yaml", n) # 将yaml中第一项会议id 写入返回yaml文件，
    request.check(redata,expectschema)

if __name__ == "__main__":
    test_start_meet_living()

