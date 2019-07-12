#coding:utf8
#from multiprocessing import Process, Queue
import os, time, random
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend
import testcase
from set_driver import set_driver
import subprocess
import getDeviceInfo
import urllib

def getport():  
    aport = random.randint(4723, 4723)  
    # 判断端口是否被占用  
    while getDeviceInfo.IsOpen('127.0.0.1', aport):  
        aport = random.randint(4723, 4723)  
    bpport = random.randint(4724, 4724)  
    while getDeviceInfo.IsOpen('127.0.0.1', bpport):  
        bpport = random.randint(4724, 4724)  
    return aport, bpport  
def getsys():  
    sys = str(random.randint(4, 6)) + "." + str(random.randint(4, 6)) + "." + "2"  
    return sys  

def download():
    url = "http://192.168.180.81:8888/56001/vtm/app/build/outputs/apk/app-debug.apk"
    f = urllib.request.urlopen(url)
    data = f.read()
    with open("F:/542demo/app-debug.apk", "wb") as code:
        code.write(data)
    f.close()

class readyH(object):  
    def __init__(self,device,path_to_apk):  
        self.device = device 
        self.path_to_apk = path_to_apk 
        #aa= getport()  
        self.ap = '4723'#aa[0]  
        #self.bp = aa[1]  
  
    def installapp(self,device,path_to_apk):  
        os.popen("adb -s {0} install {1}".format(self.device, self.path_to_apk))  
        print u"安装app完成"
        time.sleep(10)
        wq=set_driver()
        self.driver=wq.get_driver()
        time.sleep(5)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()          
        print u"授予app权限完成"
        self.driver.quit() 
    def start_appium(self):  # device_uid,  
        # appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600  
        errormsg = "" 
        appium_server_url = ""  
        try:
            host = '127.0.0.1'
            appium_log_path ='E:/appium_logs'
            ap = '4723'#getport()[0]  
            bp = '4724'#getport()[1]  
            print ap,bp,self.device  
            cmd = 'start /b appium -a '+ host +' -p '+ str(ap)+ ' --bootstrap-port '+ str(bp) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+  
            print cmd
            p = subprocess.call(cmd, shell=True,stdout=open('E:/appium_logs/logs.log','w'),stderr=subprocess.STDOUT)
            print p
            appium_server_url = 'http://' + host +':' + str(ap) +'/wd/hub'
            print appium_server_url 
        except Exception, msg:  
            errormsg = str(msg)  
    def get_driver(self):  
        desired_caps = {}  
        desired_caps['platformName'] = 'Android'  
        desired_caps['platformVersion'] = getsys()
        desired_caps['udid'] = self.device  
        #desired_caps['app'] = path_to_apk  
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao'
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity' 
        desired_caps['deviceName'] = self.device  
        url = 'http://localhost:%s/wd/hub' % str(self.ap)  
        print url  
        self.driver = webdriver.Remote(url, desired_caps)  
        return self.driver
    def disdrop(self):
        time.sleep(10)
        self.driver.close_app()
        '''
        print "close_app"
        self.driver.quit()
        print "driver.quit"
        '''
    def main_case(self):
        download() 
        #time.sleep(10)
        #self.installapp(self.device,self.path_to_apk)#path_to_apk  D:/541demo/5.4.1sc_app-debug.apk
        #time.sleep(10)
        #print u'安装app完成'
        time.sleep(10)
        #self.start_appium()
        #time.sleep(5) 
        #self.get_driver()
        #time.sleep(10)
        #self.disdrop()
        #time.sleep(5)

        #print "disdrop"
        #time.sleep(5)  
        #testcase.myCase(self.driver).case_one()  
        
    def main_case1(self):   
        self.get_driver()  
        time.sleep(5)
        #test_recive.Imtest(self.driver).test_recive()        
a=readyH('3a11d697','F:/542demo/app-debug.apk')#3a11d697 e52f9b61       
a.main_case()
#subprocess.Popen('taskkill /F /IM node.exe',shell=True)





