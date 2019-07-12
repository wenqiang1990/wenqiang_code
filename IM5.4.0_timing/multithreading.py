# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random
import test_b_send_1
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend

desired_caps = {}
desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
desired_caps['udid'] = '3a11d697' #设备的udid 实际控制启动哪台机器
desired_caps['platformName'] = 'Android'   
desired_caps['platformVersion'] = '5.1.1'   
desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao' #com.yuntongxun.eckuailiao
desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'#com.yuntongxun.ecdemo.ui.phonemodel.PhoneUI#com.yuntongxun.ecdemo.ui.account.LoginActivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
verificationErrors = []
driver.implicitly_wait(10) 


# 写数据进程执行的代码:
def send(q):
    test_b_send_1.test_send_txt(self,id='13366778604')
    q.put(value)
    time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    k=0
    while k<2:
        k=k+1
        print k
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    #pw.join()
    #pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    #pr.terminate()