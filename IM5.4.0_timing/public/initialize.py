#coding:utf-8
from appium import webdriver

def initialize(udid="aa8af450"):#13366778606
    desired_caps = {}
    desired_caps['deviceName'] = 'aa8af450'# 3a11d697 ：红米note3
    desired_caps['udid'] = udid #设备的udid 实际控制启动哪台机器
    desired_caps['platformName'] = 'Android'   
    desired_caps['platformVersion'] = '7.0'   
    desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao'  
    desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'
    driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
    verificationErrors = []
    driver.implicitly_wait(10) 