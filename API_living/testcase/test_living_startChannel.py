# coding:utf-8
import sys
sys.path.append("D:\workspace\API_living\common")
import common.api_request
import common.request_excel
import pytest,allure
excel_file='D:/workspace/API_living/params/testcase.xlsx'


excel_data = common.request_excel.open_excel(excel_file)
lines=range(len(excel_data["startChannel"]))
@pytest.mark.parametrize("line", lines)#参数化
def test_living_getlist1(line):
    excel_data = common.request_excel.open_excel(excel_file)
    excel_data = list(excel_data["startChannel"][line])  # 依次取出列表中的元组
    host = str(excel_data[2]) + ":" + str(excel_data[3])
    appid = excel_data[4]
    url = excel_data[5]
    check=excel_data[10]
    excel_data[5] = url % (host, appid)
    #print(excel_data[5])
    redata = common.api_request.api_request_excel(excel_data)
    assert redata["message"] == check
    # request.check(redata,expectschema)


#test_living_getlist1(0)