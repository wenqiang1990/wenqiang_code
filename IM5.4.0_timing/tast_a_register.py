#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend 
from clear_massage import clear_massage
from clear_massage import clear_allmassage
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_massage(self):
        '''查找联系人，发送文本消息'''
        try:
            logout.test_logout(self)#退出登录
        except:
            print "未登录，无需执行退出登录操作" 
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/bu_register").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").send_keys("13366778604")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_getcode").click()#点击获取验证码
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_yanzhengma").send_keys("222222")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").send_keys("111111")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_regi").click()#点击注册
        #print "Start : %s" % time.ctime()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_massage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      