#coding:utf-8
from appium import webdriver

class set_driver(object):  
    def __init__(self,device='3a11d697'): #S9B7N17506015085--  三星 e52f9b61  联想P1 3a11d697
        self.device = device     
    
    def get_driver(self,device='3a11d697',port='4723'):  
        desired_caps = {}
        desired_caps['deviceName'] = device 
        desired_caps['platformName'] = 'Android'  
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['udid'] = device
        #desired_caps['app'] = path_to_apk
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True" 
        desired_caps['noReset'] = "True"#用于确定是否保留登录状态，true为保留
        desired_caps['appPackage'] = 'com.yuntongxun.rongxin.lite'
        desired_caps['appActivity'] = 'com.yuntongxun.rongxin.lite.ui.LauncherUI' #com.yuntongxun.pluginexample.ui.LauncherUI
        self.driver = webdriver.Remote('http://localhost:'+ port +'/wd/hub', desired_caps)
        print(device) 
        return self.driver