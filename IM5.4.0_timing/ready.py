#coding:utf8
# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend
import testcase
import test1_recive1
import subprocess

def getport():  
    aport = '4723'  
    # 判断端口是否被占用   
    bpport = '4724'
    return aport, bpport  
def getsys():  
    sys = str(random.randint(4, 6)) + "." + str(random.randint(4, 6)) + "." + "2"  
    return sys  
  
  
class readyH(object):  
    def __init__(self,device,ap):  
        self.device = device 
        self.ap = ap 
  
    '''def installapp(self):  
        os.popen("adb install -r "+str(getApkPath.get_apk_path())) ''' 
  
    def start_appium(self):  # device_uid,  
        # appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600  
        errormsg = ""  
        appium_server_url = ""  
        try:  
            ap = '4723'  
            bp = '4724'  
            print ap,bp,self.device  
            cmd = 'appium' + ' -p ' + str(self.ap )+ ' --bootstrap-port ' + str(self.bp) + ' -U ' + str(self.device) # ' -U '+ device_uid+  
            print cmd  
            # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)  
            p = subprocess.Popen(cmd, shell=True)  
            print p  
        except Exception, msg:  
            errormsg = str(msg)  
    def get_driver(self):  
        desired_caps = {}  
        desired_caps['platformName'] = 'Android'  
        desired_caps['platformVersion'] = getsys()
        desired_caps['udid'] = self.device 
        #desired_caps['app'] = getApkPath.get_apk_path()  
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao'
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'  
        desired_caps['deviceName'] = self.device  
        url = 'http://localhost:%s/wd/hub' % str(self.ap)  
        print url  
        self.driver = webdriver.Remote(url, desired_caps)  
        return self.driver  
    def disdrop(self):  
        #self.driver.close_app()  
        self.driver.quit()  
    def main_case(self):  
        #self.installapp()  
        #time.sleep(10)  
        #self.start_appium()  
        self.get_driver()  
        time.sleep(5)
        testcase.myCase(self.driver).case_one()  
         
    def main_case1(self):   
        self.get_driver()  
        time.sleep(5)
        test1_recive1.Imtest(self.driver).test_recive()







