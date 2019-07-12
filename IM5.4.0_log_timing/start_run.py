#coding=utf-8
import os
import time

k=1
while k <2:
    now_time=time.strftime('_%M')
    if now_time == '_00' or now_time == '_30':
        print time.strftime('%H_%M')
        print u"开始运行脚本:"
        os.chdir("E:\\workspace\\IM5.4.0_log_timing")
        os.system('all-test.py') #执行脚本
        print u"运行完成退出"
    else:
        time.sleep(10)
        print time.strftime('%H_%M')
