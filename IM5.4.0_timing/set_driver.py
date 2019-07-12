#coding:utf-8
from appium import webdriver

class set_driver(object):  
    def __init__(self,device='3a11d697'): #S9B7N17506015085--  e52f9b61  
        self.device = device     
    
    def get_driver(self,device='3a11d697'):  
        desired_caps = {}
        desired_caps['deviceName'] = self.device 
        desired_caps['platformName'] = 'Android'  
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['udid'] = self.device
        #desired_caps['app'] = path_to_apk
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True" 
        desired_caps['appPackage'] = 'com.yuntongxun.rongxin.lite'
        desired_caps['appActivity'] = 'com.yuntongxun.rongxin.lite.permission.RECEIVE_MSG' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 
        return self.driver