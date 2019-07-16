#coding:utf-8
import time,os
from public.extend import Appium_Extend
from appium import webdriver
from public import tast

def test_login(self,phoneid="13366778604",password=""):#
    '''登陆'''   
    k=0
    while k<2:
        k=k+1
        try:
            wq=str(self.driver.find_element_by_name(u"登录"))#登录标签
            if wq:
                self.driver.find_element_by_accessibility_id("登 录").click()#点击登录
                self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"有会网络会议\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField").clear()
                self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"有会网络会议\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField").send_keys(phoneid)#timecode
                self.driver.find_element_by_name("输入密码").send_keys(password)
                print("账号:{} 密码:{}".format(phoneid,password))
                self.driver.find_element_by_accessibility_id("登 录").click()#点击登陆
                time.sleep(2)
                print ("点击登陆并等待了2秒")
                try:
                    self.driver.find_element_by_accessibility_id("好")
                except:
                    print("没有弹出通讯录权限提示")
        except:
            print ("账号%s登录异常" %phoneid)
       
#test_login(13366778604)
