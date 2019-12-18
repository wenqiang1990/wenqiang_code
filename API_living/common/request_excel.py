# coding:utf-8
import requests
import json
import sys
sys.path.append("..")
import xlrd


def open_excel(excel_file):
    try:
        book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    sheets = book.sheet_names()  # 获取所有sheet表名
    dict={}
    for sheet in sheets:
        sh = book.sheet_by_name(sheet)  # 打开每一张表
        row_num = sh.nrows
        print('sheet %s: '%sheet)
        print("row_num %s: " % row_num)
        list = []  # 定义列表用来存放数据
        for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sh.row_values(i)  # 按行获取excel的值
            value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], \
                     row_data[6], row_data[7], row_data[8], row_data[9], row_data[10])
            list.append(value)  # 将数据暂存在列表
            #print("i {} list{}".format(i,list))
        dict[sheet] = list
    #print(dict)
    return dict
#open_excel("D:/workspace/API_living/params/testcase.xlsx")



def interface_test(num, api_name, api_host, request_url, method,
                    request_data_type, request_data, check_point):
    # 构造请求headers
    headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                      'X-Requested-With' : 'XMLHttpRequest',
                      'Connection' : 'keep-alive',
                      'Referer' : 'http://' + api_host,
                      'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
                }
    # 判断请求方式，如果是GET，则调用get请求，POST调post请求，都不是，则抛出异常
    if method == "GET":
        r = requests.get(url=api_host+request_url, params=json.loads(request_data), headers=headers)
        # 获取请求状态码
        status = r.status_code
        # 获取返回值
        resp = r.text
        if status == 200:
            # 断言，判断设置的断言值，是否在返回值里面
            if check_point in str(r.text):
                print("第{}条用例'{}'执行成功，状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
            else:
                print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
        else:
            print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
            return status, resp
    elif method == "POST":
        # 跟GET里面差不多，就不一一注释了
        r = requests.post(url=api_host+request_url, params=json.loads(request_data), headers=headers)
        status = r.status_code
        resp = r.text
        if status == 200:
            if check_point in str(r.text):
                print("第{}条用例'{}'执行成功，状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
            else:
                print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
        else:
            print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
            return status, resp
    else:
        print("第{}条用例'{}'请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。".format(num, api_name))
        return 400, "请求方式有误"


