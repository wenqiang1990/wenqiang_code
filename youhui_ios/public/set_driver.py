#coding:utf-8
from appium import webdriver

class set_driver(object):  
    def __init__(self,device='3a11d697'): #S9B7N17506015085--  三星 e52f9b61  联想P1 3a11d697
        self.device = device     
    
    def get_driver(self,device='3a11d697',port='4723'):  
        desired_caps = {}
        desired_caps['deviceName'] = 'iPod'
        desired_caps['automationName'] = 'XCUITest'  # Xcode8.2以上无UIAutomation,需使用XCUITest
        desired_caps['platformName'] = 'IOS'
        desired_caps['platformVersion'] = '10.3.3'
        desired_caps['udid'] = device
        desired_caps['bundleId'] = 'com.yuntongxun.youhui'
        desired_caps['newCommandTimeout'] = 3600  # 1 hour
        self.driver = webdriver.Remote('http://localhost:'+ port +'/wd/hub', desired_caps)
        #print(device)
        return self.driver