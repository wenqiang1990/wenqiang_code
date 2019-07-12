#coding=utf-8
import os
import time

k=1
while k <2:
    now_time=time.strftime('%H_%M')

    '''print u"开始运行初始化脚本:"  
    os.chdir("E:\\workspace\\IM5.4.0_timing")
    os.system('ready1.py') #执行脚本
    print u"下载及安装app" 
    time.sleep(10)
    print now_time
    #now_time=time.strftime('_%M')
    os.chdir("E:\\workspace\\IM5.4.0_timing")
    os.system('all-test.py') #执行脚本'''
      
    if now_time == '00_10' or now_time == '02_10' or now_time == '04_10' or now_time == '06_10' :
        print u"开始运行测试用例脚本:"
        os.chdir("E:\\workspace\\IM5.4.0_timing")
        os.system('all-test.py') #执行脚本
        print u"运行完成退出"
    else:
        time.sleep(10)
        print now_time
                
    if now_time == '01_50' or now_time == '03_50' or now_time == '05_50' or now_time == '07_50':
        print u"开始运行清理群组数据脚本:"
        os.chdir("E:\\workspace\\IM5.4.0_timing")
        os.system('clear_group.py') #执行脚本
        print u"运行完成退出"         
    else:
        time.sleep(10)
        print now_time
        
    if now_time == '02_00' or now_time == '04_00' or now_time == '06_00' or now_time == '08_00':
        print u"开始运行清理讨论组数据脚本:"
        os.chdir("E:\\workspace\\IM5.4.0_timing")
        os.system('clear_discussion_group.py') #执行脚本
        print u"运行完成退出"         
    else:
        time.sleep(10)
        print now_time        
        
        
        
        
