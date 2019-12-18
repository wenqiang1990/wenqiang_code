# coding:utf-8
import sys
sys.path.append("D:\workspace\API_living\common")
import common.api_request
import common.request_excel
from params import schema2
import pytest
excel_file='D:/workspace/API_living/params/testcase.xlsx'

#将excel中的测试case逐条取出放入列表lines，使用pytest参数化功能，将列表中的数据逐一套入api_request函数，并且对比请求返回结果
excel_data = common.request_excel.open_excel(excel_file)
lines=range(len(excel_data["info"]))
@pytest.mark.parametrize("line", lines)#参数化
def test_living_channelInfo(line):
    excel_data = common.request_excel.open_excel(excel_file)
    excel_data = list(excel_data["info"][line])  # 依次从对应sheet页 取出列表中的元组
    host = str(excel_data[2]) + ":" + str(excel_data[3])
    appid = excel_data[4]
    url = excel_data[5]
    check=excel_data[10]
    excel_data[5] = url % (host, appid)
    #print(excel_data[5])
    redata = common.api_request.api_request_excel(excel_data)
    assert redata["message"] == check
    #common.api_request.check(redata,schema2.schema) 


#test_living_getlist1(0)