# coding:utf-8
import sys,logging,time
import test_meet_living_start
from common import globle_set
sys.path.append("..")
from common import api_request
from params import yaml_handle
logging.basicConfig(level=logging.DEBUG)

def test_stop_meet_living():
    i = yaml_handle.read_yaml("cfgyaml.yaml")
    i = i[2]  # 2是停止直播
    print(i)
    confId = globle_set.get_map("confId")
    sessionId = globle_set.get_map("sessionId")
    i["request"]["json"]["confId"] = confId # 取会议id
    i["request"]["json"]["sessionId"] = sessionId
    print(i)
    log = logging.getLogger('test_stop_meet_living')
    time.sleep(1)
    log.debug(i)
    redata = api_request.api_request(i)
    assert redata["statusCode"] == "000000"
    return redata
    #request.check(redata,expectschema)

if __name__ == "__main__":
    test_stop_meet_living()

