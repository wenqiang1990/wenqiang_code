#coding:utf-8
import time,os

def run_test():
    os.system("pytest D:\\workspace\\API_living\\testcase\\ -n 2 --reruns 1 --alluredir=D:\\workspace\\API_living\\testcase\\report_xml")#执行用例将测试结果给allure，report_xml是报告生成路径
    print('执行用例结束')
    os.system("allure generate D:\\workspace\\API_living\\testcase\\report_xml\\ -o D:\\workspace\\API_living\\testcase\\report\\ --clean")#执行用例将测试结果给allure ，report_xml是报告存放路径  新报告生成路径为默认allure-report
    print('生成报告')
    os.system("allure open -h 192.168.177.116 -p 8083 D:\\workspace\\API_living\\testcase\\report\\")  # 启动8083端口查看报告，报告路径http://127.0.0.1:8083/index.html

run_test()